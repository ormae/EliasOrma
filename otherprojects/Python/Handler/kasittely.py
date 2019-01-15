import csv
import operator

def makefloat(str):
    try:
        if(str.find(",")):
            strjono = str.split(",")
            if(len(strjono)> 1):
                intstr = strjono[0] + "." +  strjono[1]
                return float(intstr)
            return float(strjono[0])
    except AttributeError:
        return str
    except ValueError:
        return -1000

def correct(x):
    if(x == ""):
        return ""


    if(x[len(x)-1]=="\n"):
        return x[0:len(x)-1]
    elif(x == '#JAKO/0!'):
        pass
    return x



# dict tunnusluku, sortattu lista tuplena (nimi,arvo)
def teeyhdistetty(dict):
    yhdtunpisteet = {}
    for tunnusluku in dict:
        laskuri = 1
        for piece in dict[tunnusluku]:
            name = piece[0]
            if(yhdtunpisteet.get(name) == None):
                yhdtunpisteet[name] = laskuri
            else:
                yhdtunpisteet[name] += laskuri
            laskuri += 1

    limit = len(yhdtunpisteet)*1/3
    round = 1


    uusitldict = {}

    for firma in sorted((yhdtunpisteet).items(), key=operator.itemgetter(1)):
        if(round > limit):
            break
        else:
            uusitldict[firma[0]] = 0
        round += 1

    return uusitldict


def read(fileName):
    toOpen = fileName + '.csv'
    textdict = {}
    innerdict = {}
    yearslist = []
    named = False
    with open(toOpen, encoding="utf-8-sig") as csvfile:
        try:
            line = csvfile.readline()

            linelist = line.split(";")
            yearindex = 1
            if (named == False):
                while (yearindex != len(linelist)):
                    a = correct(linelist[yearindex])
                    yearslist.append(a)
                    yearindex += 1
                named = True

            line = csvfile.readline()
            linelist = line.split(";")

            usedindex = 0
            while (len(linelist) != 1):
                try:
                    for i in linelist[1:]:
                        innerdict[yearslist[usedindex]] = correct(i)
                        usedindex += 1
                    usedindex = 0
                except IndexError:
                    print("!")

                textdict[correct(linelist[0])] = innerdict

                line = csvfile.readline()
                linelist = line.split(";")
                innerdict = {}
            #for a in textdict:
                #print(a, textdict[a])


        except csv.Error:
            print("\n"
                  "The given dialect is wrong.")
        return textdict



def readfirmat():
    yearslist = []
    named = False

    with open("firmalista.csv", encoding="utf-8-sig") as csvfile:
        line = csvfile.readline()

        linelist = line.split(";")
        yearindex = 0
        if (named == False):
            while (yearindex != len(linelist)):
                a = correct(linelist[yearindex])
                yearslist.append(a)
                yearindex += 1
            named = True
        line = csvfile.readline()
        linelist = line.split(";")

        usedindex = 0

        yeardict = {}

        rounds = 1
        while (len(linelist) != 1):

            try:
                for i in linelist:
                    i = correct(i)
                    if(i != ""):

                        if(yeardict.get(yearslist[usedindex]) == None):
                            yeardict[yearslist[usedindex]] = []
                        yeardict[yearslist[usedindex]].append(i)
                    usedindex += 1
                usedindex = 0
            except IndexError:
                print("!")

            line = csvfile.readline()
            linelist = line.split(";")
            rounds += 1



        return yeardict

def writefile(paadict):
    try :
        with open('tuloskset.csv',"w",newline='') as csvfile:

            try:
                # vuosi, tunnusluku, dict nimi : value
                writecsv = csv.writer(csvfile,delimiter=';')


                vuodet = []
                for vuosi in paadict:
                    vuodet.append(vuosi)
                    for a in range(4):
                        vuodet.append("")
                #writecsv.writerow(vuodet)

                tunnusluvut = []
                for vuosi in paadict:
                    for tl in paadict[vuosi]:
                        tunnusluvut.append(tl)
                #writecsv.writerow(tunnusluvut)

                ggline = []
                tupledict = {}
                for vuosi in paadict:
                    if(tupledict.get(vuosi) == None):
                        tupledict[vuosi] = {}
                    for tl in paadict[vuosi]:
                        print(paadict[vuosi][tl])
                        tupledict[vuosi][tl] = sorted(paadict[vuosi][tl],
                                                      key=operator.itemgetter(1),reverse=True)

                line = []
                for vuosi in paadict:
                    writecsv.writerow(list(vuosi))

                    for tl in paadict[vuosi]:
                        line.append(tl)

                        for firma in paadict[vuosi][tl]:
                            line.append(firma)
                            #line.append(paadict[vuosi][tl][firma])
                        writecsv.writerow(line)
                        line = []
                    writecsv.writerow("")


            except csv.Error:
                print("\n"
                    "The given dialect is wrong.")
                return

        print("\n"
            "File has been converted")

    except OSError or csv.Error:

        print("\n"
            "There was an error in handling the file.")


def main():

    kaikkitunnusluvut = {}

    tunnusluvut = ["EBITDAEV","EP","BP"]
    #muotoa tunnusluku,firmannimi,vuosi:value
    kaikkitunnusluvut["EBITDAEV"] = read("EBITDAEV")
    print(" ")
    kaikkitunnusluvut["EP"] = read("EP")
    print(" ")
    kaikkitunnusluvut["BP"] = read("BP")




    #muotoa vuosi,firma
    päädict = readfirmat()


    # vuosi, tunnusluku, dict nimi : value
    kayttodicti = {}
    for vuosi in päädict:
        for firma in päädict[vuosi]:
            if(kayttodicti.get(vuosi) == None):
                kayttodicti[vuosi] = {}
            for tunnusluku in tunnusluvut:
                if(kayttodicti[vuosi].get(tunnusluku) == None):
                    kayttodicti[vuosi][tunnusluku] = {}
                kayttodicti[vuosi][tunnusluku][firma] = \
                    makefloat(kaikkitunnusluvut[tunnusluku][firma][vuosi])

    # graham == EP*BP
    validict = {}
    for vuosi in kayttodicti:
        for a in kayttodicti[vuosi]["EP"]:
            num = makefloat(kayttodicti[vuosi]["EP"][a]) * makefloat(kayttodicti[vuosi]["BP"][a])
            validict[a] = num
        limit = len(validict) * 1 / 3
        counter = 1
        for b in sorted(validict.items(),
                             key=operator.itemgetter(1),reverse=True):
            if(counter > limit):
                break
            if(kayttodicti[vuosi].get("Graham") == None):
                kayttodicti[vuosi]["Graham"] = {}
            kayttodicti[vuosi]["Graham"][b[0]] = validict[b[0]]
            counter += 1
        validict = {}



    # yhd t3 == kolme tunnuslukua
    tluvutkaytto = {}
    for vuosi in kayttodicti:
        for tunnusluku in kayttodicti[vuosi]:
            tluvutsorted = sorted(kayttodicti[vuosi][tunnusluku].items(), key=operator.itemgetter(1),reverse=True)
            tluvutkaytto[tunnusluku] = tluvutsorted
        kayttodicti[vuosi]["yhdT3"] = teeyhdistetty(tluvutkaytto)



    # Poista kolmasosa origluvuista
    alkuperaisetSuodatettu = {}
    for vuosi in kayttodicti:
        for tl in kayttodicti[vuosi]:
            if(tl != 'yhdT3' and tl != 'Graham'):
                limit = len(kayttodicti[vuosi][tl]) * 1 / 3
                counter = 1
                for a in sorted(kayttodicti[vuosi][tl].items(),
                                key=operator.itemgetter(1), reverse=True):
                    if (counter > limit):
                        break
                    alkuperaisetSuodatettu[a[0]] = a[1]
                    counter += 1
                kayttodicti[vuosi][tl] = alkuperaisetSuodatettu
                alkuperaisetSuodatettu = {}

    writefile(kayttodicti)

main()