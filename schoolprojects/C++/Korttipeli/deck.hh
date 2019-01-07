#ifndef DECK_HH
#define DECK_HH

#include <vector>
#include <QFrame>
#include "card.hh"
#include "opendeck.hh"

class OpenDeck;
class Deck : public QFrame
{
    Q_OBJECT

public:
    Deck(OpenDeck* openDeck,QWidget *parent = 0);

    // Korttipakasta voi nostaa päällimmäisen kortin.
    Card* pickCard();


    // TODO: Lisää tähän uusia toimintoja, joita korttipakalle voi suorittaa.

    // Sekoittaa korttipakan
    void shuffle();


signals:
    // Signaali, jonka pakka lähettää, kun kortti nostetaan.
    void cardPicked(Card* card);


protected:
    // Itse toteutettu Qt:n widgetin klikkaamiseen liittyvä metodi.
    void mousePressEvent(QMouseEvent *event);

private:
    // Korttipakan sisältämät kortit.
    std::vector<Card*> cards_;
    OpenDeck* pickedCards_;
};

#endif // DECK_HH
