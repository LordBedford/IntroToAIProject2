# Andrew Cater

from tkinter import *
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
        self.colors = self.colors = ["green", "blue", "purple", "orange", "blue", "purple", "orange","black"]
        self.startX = 40
        self.startY = 40
        self.hand = (-1,-1)
        self.pieces = ["hero","wumpus","wizard"]

    def tick(self):
        self.window.update()

    def startScreen(self):
        self.frame = Frame(self.window, width=1000, height=1000)
        self.frame.pack()
        self.startButton = Button(self.frame, text='START GAME!', width=25,command = self.gameSetup)
        self.startButton.place(x=500, y=500)
        self.gameSize = Text(self.frame, height=1, width=25)
        self.gameSize.place(x=500, y=600)

    def gameSetup(self):
        self.frame.destroy()
        self.frame = Frame(self.window, width=1000, height=1000)
        print("yeet")
        self.frame.pack()
        self.map.append([1,2,3])
        self.map.append([0,7,0])
        self.map.append([4,5,6])#Replace with map generator
        self.drawMap()

    def drawMap(self):
        for i  in range(len(self.map)):#i is y
            for j in range(len(self.map[i])):#j is x
                (self.c.create_rectangle(self.startX + (40 * (j)), self.startY + (40 * (i)),self.startX + (40 * (j+1)), self.startY + (40 * (i+1)),
                                         fill=self.colors[int(self.map[i][j])],
                                         outline='black'))
        self.c.pack()
    def leftHandler(self, event):
        print("Left clicked at:", event.x, event.y)
        y = int(((event.y - (event.y % 40))-self.startY)/40)
        x = int(((event.x - (event.x % 40))-self.startX)/40)
        selected = self.map[y][x]
        print(int(((event.y - (event.y % 40))-self.startY)/40))
        print(int(((event.x - (event.x % 40))-self.startX)/40))
        if selected == 0:
            print("Grass")
        elif selected == 1 or selected == 4:
            print("Hero")
        elif selected == 2 or selected == 5:
            print("Wumpus")
        elif selected == 3 or selected == 6:
            print("Wizard")
        elif selected == 7:
            print("Pit")
        else:
            print("dab")
        if selected == 1 or selected  == 2 or selected == 3:
            if self.hand[0] == -1 and self.hand[1] == -1:#activates if your not holding a piece
                print("You picked up a", self.pieces[selected-1])
                self.hand = (y,x)
        elif selected == 0 and self.hand != (-1,-1):
            if (self.hand[0] - y <= 1 or self.hand[0] - y >= -1)and(self.hand[1] - x <= 1 or self.hand[1] - x >= -1):
                self.map[y][x] = self.map[self.hand[0]][self.hand[1]]
                self.map[self.hand[0]][self.hand[1]] = 0
                self.hand = (-1, -1)
                self.drawMap()


    def rightHandler(self, event):
        print("Right clicked at:", event.x, event.y)
        print("Hand Emptied")
        self.hand = (-1,-1)
