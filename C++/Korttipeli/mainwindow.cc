#include <QFrame>
#include <QHBoxLayout>
#include <stdlib.h> // rand

#include "mainwindow.hh"
#include "cardslot.hh"

// Vakiot layouttia varten
unsigned int const NUMBER_OF_MIDDLESLOTS = 5;
unsigned int const MAX_CARDS_SETREADY = 3;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    setSizePolicy(QSizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed));
    setupLayout();
    connect(deck_, &Deck::cardPicked, pickedCards_, &OpenDeck::addCard);
}

MainWindow::~MainWindow()
{
}

void MainWindow::setupLayout()
{
    // Pääikkunan isoimpana rakenteena on frame, joka sisältää...
    QFrame* frame = new QFrame;
    QVBoxLayout* frameLayout = new QVBoxLayout(frame);

    // ... ala, keski ja ylärivin.


    // TODO: SPACELAYOUT TEKSTI, TILAN LISÄYS, PISTEET, VOITTO
    QHBoxLayout* topRowLayout = new QHBoxLayout();
    QHBoxLayout* middleRowLayout = new QHBoxLayout();
    QHBoxLayout* bottomRowLayout = new QHBoxLayout();
    QHBoxLayout* spaceLayout = new QHBoxLayout();

    frameLayout->addLayout(topRowLayout);
    frameLayout->addLayout(middleRowLayout);
    frameLayout->addLayout(bottomRowLayout);
    frameLayout->addLayout(spaceLayout);


    // Luodaan pakkaoliot.
    pickedCards_ = new OpenDeck(this);
    deck_ = new Deck(pickedCards_, this);


    // Lisätään yläriville suljettu ja avoin pakka...
    topRowLayout->addWidget(deck_);
    topRowLayout->addWidget(pickedCards_);

    // Lisätään keskiriville valmiiksi (Tämäntiedoston alussa) määritelty määrä
    // Cards slotteja, missä kussakin on samat säännöt.
    // Samassa loopissa lisätään myös cardslotteihin satunnainen määrä kortteja
    // Jotka eivät ole auki. (Yläraja määritelty myös tiedoston alussa.

    for (int middleslots = 0; middleslots != NUMBER_OF_MIDDLESLOTS; middleslots++)
    {
        int randomcardadd = rand() % MAX_CARDS_SETREADY;
        CardSlot* newcardslot = new CardSlot(&GameRules::checkCardSuitNum, false, this);
        for(int addcards = 0; addcards != randomcardadd+1; ++addcards)
        {
            Card* newcard = deck_->pickCard();
            newcardslot->addCard(newcard);
        }
        // Käänntetään korttipinon päällimmäinen kortti
        newcardslot->flipTop();
        middleRowLayout->addWidget(newcardslot);
        setCentralWidget(frame);
    }

    // Alariviin asetetaan 4 cardslottia (Yksi jokaiselle maalle).
    // TODO: Tähän korttiriviin voi asettaa vain saman maan kortteja
    // järjestyksessä 1-13. Kortit pinoutuvat päällekkäin.
    for (int bottomslots = 0; bottomslots != 4; bottomslots++)
    {
        bottomRowLayout->addWidget(new CardSlot(&GameRules::checkIfSuitNext, true, this));
        setCentralWidget(frame);
    }

    // Teksti labeli voittoilmoitusta varten. EI TOTEUTETTU.
    text_ = new QLabel();
    QFont font = text_->font();
    font.setPointSize(72);
    font.setBold(true);
    text_->setFont(font);
    topRowLayout->addWidget(text_);

}
