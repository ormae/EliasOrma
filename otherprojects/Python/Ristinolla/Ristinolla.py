from tkinter import *
import random
import time
import winsound

from tkinter import messagebox

IMAGES = ["0.gif","1.gif","2.gif"]
PELAAJA_O = "0"
PELAAJA_X = "1"



class Ristinolla:
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Ristinolla")

        self.__kuvat = []
        for i in IMAGES:
            kuva = PhotoImage(file=i)
            self.__kuvat.append(kuva)

        self.__totalwins= [0,0]
        self.__rounds_played = 0

        self.__vuoro = random.randint(0, 1)
        if self.__vuoro == 1:
            self.__first_turn = "X"
        else:
            self.__first_turn = "O"



        self.__infotext = Label(self.__ikkuna,text = "Player {},turn".format(self.__first_turn))
        self.__infotext.grid(row = 4,column = 2)
        self.__infotext2 = Label(self.__ikkuna,text = "Total wins Player X: {},"
                                                      "\n"
                                                      "Player O: {}"
                                 .format(self.__totalwins[1],self.__totalwins[0]))
        self.__infotext2.grid(row=4, column=3,sticky=E)


        self.__pointstatus = {0:[2,2,2],1:[2,2,2],2:[2,2,2]}
        self.__piclabels = {}
        self.__lambda_dict = {0: {0: lambda: self.change_status(0, 0),
                                  1: lambda: self.change_status(0, 1),
                                  2: lambda: self.change_status(0, 2)},
                              1: {0: lambda: self.change_status(1, 0),
                                  1: lambda: self.change_status(1, 1),
                                  2: lambda: self.change_status(1, 2)},
                              2: {0: lambda: self.change_status(2, 0),
                                  1: lambda: self.change_status(2, 1),
                                  2: lambda: self.change_status(2, 2)}}

        for i in range(3):
            self.__piclabels[i] = {}
            for f in range(3):
                uusi_label = Button(self.__ikkuna,command = self.__lambda_dict[i][f],image=self.__kuvat[2])
                uusi_label.grid(row=0 + f, column=2 + i, sticky=W)
                self.__piclabels[i][f] = uusi_label



    def initialize_game(self):

        for i in self.__piclabels:
            for f in self.__piclabels[i]:
                self.__piclabels[i][f].configure(image=self.__kuvat[2])

        self.__pointstatus = {0: [2, 2, 2], 1: [2, 2, 2], 2: [2, 2, 2]}

        self.__rounds_played = 0

        self.__vuoro = random.randint(0, 1)
        if self.__vuoro == 1:
            self.__first_turn = "X"
        else:
            self.__first_turn = "O"
        self.__infotext2.configure(text = "Total wins Player X: {},\n Player O: {}"
                                 .format(self.__totalwins[1],self.__totalwins[0]))

    def change_status(self,y,x):
        if self.__pointstatus[y][x] == 2:

            self.__piclabels[y][x].configure(image = self.__kuvat[self.__vuoro])
            self.__pointstatus[y][x] = self.__vuoro
            self.__rounds_played += 1

            self.check_win()

            if self.__rounds_played == 9:
                self.tie()


            elif self.__vuoro == 1:
                self.__vuoro = 0
                self.__infotext.configure(text="Player O,turn")

            else:
                self.__vuoro = 1
                self.__infotext.configure(text="Player X,turn")



    def check_win(self):
        a = self.__vuoro
        dict = self.__pointstatus

        for situation in dict:
            if dict[situation] == [a,a,a]:
                self.win()

        for i in range(3):
            if (dict[0][i] == a and dict[1][i] == a and dict[2][i] == a):
                self.win()

        if (dict[0][0]== a and dict[1][1]== a and dict[2][2] == a):
            self.win()

        if (dict[0][2]== a and dict[1][1]== a and dict[2][0] == a):
            self.win()

    def win(self):
        if self.__vuoro == 1:
            winner = "X"
            self.__totalwins[1] += 1

        else:
            winner = "O"
            self.__totalwins[0] += 1

        messagebox.showinfo("{} WON!".format(winner),
                            "Player {} won the match. A newgame has been started"
                            .format(winner))

        self.initialize_game()


    def tie(self):
        messagebox.showinfo("TIE","The match is a tie. A newgame has been started")
        self.initialize_game()

    def start(self):
        self.__ikkuna.mainloop()

def main():
    ui = Ristinolla()
    ui.start()
main()