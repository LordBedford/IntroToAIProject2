# Andrew Cater

from tkinter import *

from PIL import ImageTk as itk, Image
import MapCreator
import random
from tkinter import messagebox


import numpy as np
# import astarSearch
import os


class MapMaker:

    def __init__(self):
        self.window = Tk()
        self.labels = []
        # Creates the window of set size
        self.window.bind("<Button-1>", self.leftHandler)
        self.window.bind("<Button-3>", self.rightHandler)
        self.frame = Frame()
        self.frame.pack()
        self.c = Canvas(self.frame, width=1000, height=1000)
        self.map = []
        self.colors = self.colors = ["green", "blue", "purple", "orange", "blue", "purple", "orange", "black"]
        self.startX = 40
        self.startY = 40
        self.hand = (-1, -1)
        self.pieces = ["hero", "wumpus", "wizard"]
        self.size = 3
        self.turn = 0
        self.gameStarted = FALSE
        self.squareSize = 40
        hero = Image.open("Hero.PNG")
        wumpus = Image.open("Wumpus.PNG")
        wizard = Image.open("Wizard.PNG")
        hero = hero.resize((self.squareSize, self.squareSize))
        wumpus = wumpus.resize((self.squareSize, self.squareSize))
        wizard = wizard.resize((self.squareSize, self.squareSize))
        self.imgs = [None, (itk.PhotoImage(hero)),(itk.PhotoImage(wumpus)),(itk.PhotoImage(wizard)),(itk.PhotoImage(hero)),
                     (itk.PhotoImage(wumpus)),(itk.PhotoImage(wizard))]

    def tick(self):
        self.window.update()

    def startScreen(self):
        self.frame = Frame(self.window, width=1000, height=1000)
        self.frame.pack()
        self.startButton = Button(self.frame, text='START GAME!', width=25, command=self.gameSetup)
        self.startButton.place(x=500, y=500)
        self.gameSize = Text(self.frame, height=1, width=25)
        self.gameSize.place(x=500, y=600)

    def gameSetup(self):
        tempSize = self.gameSize.get("1.0","end")
        tempSize = int(tempSize.strip())
        if tempSize - (tempSize%3) != 0:
            self.size = tempSize - (tempSize%3)
            self.frame.destroy()
            self.frame = Frame(self.window, width=1000, height=1000)
            print("yeet")
            self.frame.pack()
            self.map = MapCreator.mapGen(self.size)  # Replace with map generator
            self.drawMap()
            self.gameStarted = TRUE
        else:
            print("Please enter a valid number")

    def drawMap(self):
        for i in range(len(self.map)):  # i is y
            for j in range(len(self.map[i])):  # j is x
               # if self.map[i][j] == 0 or self.map[i][j] == 7:
                    (self.c.create_rectangle(self.startX + (self.squareSize * (j)), self.startY + (self.squareSize * (i)),
                                             self.startX + (self.squareSize * (j + 1)), self.startY + (self.squareSize * (i + 1)),
                                             fill=self.colors[int(self.map[i][j])],
                                             outline='black'))
               # else:
                #    lable = Label(self.frame)
                 #   lable.image = self.imgs[self.map[i][j]]
                   # lable.config(image = self.imgs[self.map[i][j]])
                    #lable.place(relx = (self.startX + (self.squareSize * (j))), rely =(self.startY + (self.squareSize * (i))))
                    #lable.pack()

        self.c.pack()

    def leftHandler(self, event):
        if self.gameStarted:
            print("Left clicked at:", event.x, event.y)
            y = int((event.y - self.startY - ((event.y - self.startY) % self.squareSize)) / self.squareSize)
            x = int((event.x - self.startX - ((event.x -self.startX) % self.squareSize)) / self.squareSize)
            if self.startX <= event.x <= self.startX + (self.squareSize*self.size) and self.startY <= event.y <= self.startY + (self.squareSize*self.size):
                selected = self.map[y][x]
                print(x)
                print(y)
                if selected == 1 or selected == 2 or selected == 3:
                    if self.hand[0] == -1 and self.hand[1] == -1:  # activates if your not holding a piece
                        print("You picked up a", self.pieces[selected - 1])
                        self.hand = (y, x)
                elif (self.hand != (-1, -1)) and ((1 >= self.hand[0] - y >= -1) and (
                        1 >= self.hand[1] - x >= -1)):
                    if selected == 0:
                        self.moveOnToGrass(y, x)
                    elif (selected == 7):
                        self.moveOnToPit(y, x)
                    elif selected == 4 or selected == 5 or selected == 6:
                        self.combat(y, x)
                else:
                    print("Failure")

    def moveOnToGrass(self, y, x):
        self.map[y][x] = self.map[self.hand[0]][self.hand[1]]
        self.map[self.hand[0]][self.hand[1]] = 0
        self.hand = (-1, -1)
        self.drawMap()

    def moveOnToPit(self, y, x):
        self.map[self.hand[0]][self.hand[1]] = 0
        self.hand = (-1, -1)
        self.drawMap()

    def combat(self, y, x):
        if self.map[y][x] == self.map[self.hand[0]][self.hand[1]]+3:
            self.map[y][x] = 0
            self.map[self.hand[0]][self.hand[1]] = 0
            self.hand = (-1, -1)
            self.drawMap()
        elif self.map[self.hand[0]][self.hand[1]] == 1:
            if self.map[y][x] == 5:
                self.map[y][x] = self.map[self.hand[0]][self.hand[1]]
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                print("Hero kills wumpus")
                self.drawMap()
            elif self.map[y][x] == 6:
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                self.drawMap()
        elif self.map[self.hand[0]][self.hand[1]] == 2:
            if self.map[y][x] == 6:
                self.map[y][x] = self.map[self.hand[0]][self.hand[1]]
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                self.drawMap()
            elif self.map[y][x] == 4:
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                self.drawMap()
        elif self.map[self.hand[0]][self.hand[1]] == 3:
            if self.map[y][x] == 4:
                self.map[y][x] = self.map[self.hand[0]][self.hand[1]]
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                self.drawMap()
            elif self.map[y][x] == 5:
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                self.drawMap()
        self.checkWinner()

    def checkWinner(self):
        count = (0,0)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if (self.map[i][j] == 1) or (self.map[i][j] == 2) or (self.map[i][j] == 3):
                    print("YEETS ASDFHHFHH",count[0])
                    count = (count[0] + 1, count[1])
                elif (self.map[i][j] == 4) or (self.map[i][j] == 5) or (self.map[i][j] == 6):
                    count = (count[0], count[1]+1)
        if count[0] != 0 and count[1] == 0:
            print("Human Player Wins!")
            self.window.destroy()
        elif count[0] == 0 and count[1] != 0:
            print("AI Player Wins!")
            self.window.destroy()
        elif count[0] == 0 and count[1] == 0:
            print("TIE!")
            self.window.destroy()

    def rightHandler(self, event):
        print("Right clicked at:", event.x, event.y)
        print("Hand Emptied")
        self.hand = (-1, -1)
