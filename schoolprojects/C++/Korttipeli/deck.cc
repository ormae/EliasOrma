#include "deck.hh"

#include <QDrag>
#include <QDragEnterEvent>
#include <QMimeData>
#include <QPainter>
#include <QLabel>
#include <algorithm> //random_shuffle


Deck::Deck(OpenDeck* openDeck,QWidget *parent) : QFrame(parent), pickedCards_(openDeck)
{
    setMinimumSize(180, 260);
    setMaximumSize(180, 260);
    setFrameStyle(QFrame::Sunken | QFrame::StyledPanel);
    for (int suit = SPADE; suit != SUIT_COUNT; ++suit){

        for (unsigned value = 1; value <= 13; ++value){
            auto card = new Card(static_cast<CardSuit>(suit), value, this);
            int xOffset = (this->width() - card->width()) / 2;
            int yOffset = (this->height() - card->height()) / 2;
            card->move(xOffset, yOffset);
            cards_.push_back(card);
        }
    }
    // Lisätty pakan sekoitus, kun pakka alustetaan.
    shuffle();
}

Card* Deck::pickCard()
{
    if (cards_.empty()){
        return nullptr;
    } else {
        Card* card = cards_.back();
        cards_.pop_back();
        return card;
    }
}

// Sekoittaa pakan.
void Deck::shuffle()
{
    std::random_shuffle(cards_.begin(), cards_.end());
}

// Suoritetaan, kun pakkaa klikataan.
void Deck::mousePressEvent(QMouseEvent *event)
{
    // Ohjelma ei saa kaatua tyhjän pakan klikkaukseen.
    if (cards_.empty()){

        // TODO: Käännäpakka
        // Siirretään kortit avoimesta pakasta suljettuun pakkaan.
        pickedCards_->getCards(cards_);

        // Asetetaan korteille suljettu pakka parentiksi, käännetään
        // kortit ja näytetään ne
        for (Card* card : cards_)
        {
            card->setParent(this);
            card->turn();
            card->show();
        }
        return;
    }

    // Otetaan osoittimen päähän pakan päällimmäinen kortti ja poistetaan se pakasta.
    Card* card = cards_.back();
    cards_.pop_back();

    // Ilmoitetaan, että pakasta otettiin kortti.
    emit cardPicked(card);

    // Hyväksytään klikkaus, koska se käsitellään aina tässä metodissa.
    event->accept();
}
