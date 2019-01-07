#ifndef GAMERULES_HH
#define GAMERULES_HH
#include <string>

namespace GameRules {

    // Kaksi seuraavaa funktiota olisi voinut toteuttaa yhdellä funktiolla
    // Pelin rakennetta olisi pitänyt täten muuttaa todella paljon kyseisten
    // Funktiokutsujen takia.

    // Tarkitaa onko päälle asetettava kortti samaamaata / yhden numeron
    // pienempi kuin allaoleva kortti.
    bool checkCardSuitNum(std::string bottom, std::string top);

    // Tarkitaa onko päälle asetettava kortti samaamaata / yhden numeron
    // suurempi kuin allaoleva kortti.
    bool checkIfSuitNext(std::string bottom, std::string top);
}

#endif // GAMERULES_HH
