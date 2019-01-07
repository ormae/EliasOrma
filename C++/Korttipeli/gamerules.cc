#include "gamerules.hh"
#include "card.hh"



// Funktio saa parametrinaan alla olevan kortin ja päälle tulevan kortin
// tiedot merkkijonomuodossa.
// Tarkistaa onko kortti jota yritetään asettaa päälle samaa
// maata kuin pohjalla oleva kortti, jos korttipaikka on tyhjä, voi siihen
// asettaa vain 13 - numero kortteja.
bool GameRules::checkCardSuitNum(std::string bottom, std::string top)
{
    std::string suitStringtop = top.substr(top.find_first_of(",")+1,1);
    std::string numStringtop = top.substr(0,top.find_first_of(","));

    // Jos cardslot on tyhjä ja pelaajan asetettava kortti on 13,
    // Lisätään se pakan päällimmäiseksi.
    if (bottom == "")
    {
        return stoi(numStringtop) == 13;
    }

    // Jos cardslotissa on jo jotain, tarkistetaan onko lisättävä kortti samaa
    // maata edellisen kortin kanssa.
    std::string suitStringbot = bottom.substr(bottom.find_first_of(",")+1,1);

    if (stoi(suitStringtop) == stoi(suitStringbot))
    {
        // Tarkistetaan onko se seuraava kortti järjestyksessä 1-13 ja
        // palautetaan false jos ei ole.
        std::string numStringbot = bottom.substr(0,bottom.find_first_of(","));
        return stoi(numStringbot)-1 == stoi(numStringtop);
    }

    // Jos kortti ei täytä ehtoja, palautetaan false.
    return false;

}

// Funktio saa parametrinaan alla olevan kortin ja päälle tulevan kortin
// tiedot merkkijonomuodossa.
// Metodi tarkastaa onko cardslot tyhjä ja lisää kortin jos sen arvo on 1.
// Metodi sallii saman maisten korttien pakan täyttämisen järjestyksessä 1-13
bool GameRules::checkIfSuitNext(std::string bottom, std::string top)
{
    std::string suitStringtop = top.substr(top.find_first_of(",")+1,1);
    std::string numStringtop = top.substr(0,top.find_first_of(","));

    // Jos cardslot on tyhjä ja pelaajan asetettava kortti on 1,
    // Lisätään se pakan päällimmäiseksi.
    if (bottom == "")
    {
        return stoi(numStringtop) == 1;
    }

    // Jos cardslotissa on jo jotain, tarkistetaan onko lisättävä kortti samaa
    // maata edellisen kortin kanssa.
    std::string suitStringbot = bottom.substr(bottom.find_first_of(",")+1,1);

    if (stoi(suitStringtop) == stoi(suitStringbot))
    {
        // Tarkistetaan onko se seuraava kortti järjestyksessä 1-13 ja
        // palautetaan false jos ei ole.
        std::string numStringbot = bottom.substr(0,bottom.find_first_of(","));
        return stoi(numStringbot)+1 == stoi(numStringtop);
    }

    // Jos kortti ei täytä ehtoja, palautetaan false.
    return false;

}
