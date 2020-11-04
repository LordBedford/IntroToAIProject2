#Andrew Cater

from tkinter import *
import random
from tkinter import messagebox

import numpy as np
import MapCreator
#import astarSearch
import os


class MapMaker:

    def __init__(self):
        self.window = Tk()
        self.labels = []
        #Creates the window of set size
        self.c = Canvas(self.window, width=1500, height=900)
        self.c.pack()

        self.colors = ["black", "green", "orange", "blue", "white", "cyan", "red"]
        #initializes buttons on the window
        self.button = Button(self.window, text='New Map', width=25, command=self.newMap)
        self.button3 = Button(self.window, text='Load Map type and number ->', width=25, command=self.load)
        self.button.place(x=0, y=0)
        self.button3.place(x=400, y=0)
        self.button2 = Button(self.window, text='Run Astar Search', width=25, command=self.getAstar)
        self.button2.place(x=800, y=100)
        self.button4 = Button(self.window, text='Run Weighted Astar Search', width=25, command=self.getWeightedAstar)
        self.button4.place(x=800, y=200)
        self.button5 = Button(self.window, text='Run Sequential Heuristic Search', width=25, command=self.getSequentialHeuristic)
        self.button5.place(x=800, y=300)
        self.button6 = Button(self.window, text='Run Uniform Cost Search', width=25, command=self.getUniformCost)
        self.button6.place(x=800, y=400)
        #initializes the text fields on the window
        self.loadbox = Text(self.window, height = 1, width = 25)
        self.loadbox.place(x=600,y=0)
        self.loadbox2 = Text(self.window, height=1, width=25)
        self.loadbox2.place(x=800, y=0)
        self.weightedastar = Text(self.window, height=1, width=25)
        self.weightedastar.place(x = 800, y = 275)
        self.heuristic1 = Text(self.window, height=1, width=25)
        self.heuristic1.place(x=800, y=375)
        self.heuristic2 = Text(self.window, height=1, width=25)
        self.heuristic2.place(x=1000, y=375)

        self.window.bind("<Button-1>", self.mouseHandler)

        self.saves = 0
        #initializes the G, H, and F labels on the window
        self.labelSelected = Label(self.window, text="Click on a cell to get its G,H, and F values")
        self.labelSelected.place(x = 1200, y = 0)
        self.labelGText = StringVar()
        self.labelFText = StringVar()
        self.labelHText = StringVar()
        self.labelGText.set("G Value:")
        self.labelHText.set("H Value:")
        self.labelFText.set("F Value:")
        self.labelG = Label(self.window, textvariable = self.labelGText)
        self.labelG.place(x=1200, y=100)
        self.labelH = Label(self.window, textvariable=self.labelHText)
        self.labelH.place(x=1200, y=200)
        self.labelF = Label(self.window, textvariable = self.labelFText)
        self.labelF.place(x=1200, y=300)
        self.labelweight1 = Label(self.window, text = "Astar Weight")
        self.labelweight1.place(x=800, y=250)
        self.labelweight2 = Label(self.window, text =  "Heuristic Weight 1")
        self.labelweight2.place(x=800, y=350)
        self.labelweight3 = Label(self.window, text ="Heuristic Weight 2")
        self.labelweight3.place(x=1000, y=350)

        self.start = []
        self.end = []

    #Redraws the map based on the current self.map value
    def updatewindow(self):
        print("UPDATING")
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                (self.c.create_rectangle(5 * (i + 2), 5 * (j + 8), 5 * (i + 3), 5 * (j + 9),
                                         fill=self.colors[int(self.map[i][j])],
                                         outline='black'))
                self.c.pack()
    #Updates the window every tick.
    def tick(self):
        self.window.update()

    #Depreciated Method
    def save(self):
       # for i in range(len(self.map)):
        #    np.savetxt(self.savefile, self.map[i], fmt='%s',newline=' ')
        temp = np.array(self.map)
        np.savetxt(self.savefile, temp, fmt='%s')
        print("Saved!")
        self.saves = self.saves + 1

    #Loads a map from the selected file
    def load(self):
        getType = (self.loadbox.get("1.0","end"))
        getType = int(getType.strip())
        getMap = (self.loadbox2.get("1.0", "end"))
        getMap = int(getMap.strip())
        tempCol = []
        tempFile = open("maps/map%s/map%s.txt" % (getType-1,getMap-1), 'r')
        i = 1
        for lines in tempFile.readlines():
            if i > 10:
                lines = lines.strip()
                tempRow = []
                for num in lines:
                    if not (num == ' '):
                        tempRow.append(num)
                tempCol.append(tempRow)
            elif i == 1:
                tempVal = 0
                lines = lines.strip()
                tempRow = []
                for num in lines:
                    if not (num == ' '):
                        tempVal = tempVal*10 + int(num)
                    else:
                        tempRow.append(tempVal)
                        tempVal = 0
                print(tempRow)
                tempRow.append(tempVal)
                self.start = tempRow
            elif i == 2:
                tempVal = 0
                lines = lines.strip()
                tempRow = []
                for num in lines:
                    if not (num == ' '):
                        tempVal = tempVal * 10 + int(num)
                    else:
                        tempRow.append(tempVal)
                        tempVal = 0
                tempRow.append(tempVal)
                self.end = tempRow

            i += 1

        self.map = tempCol
        # for i in range(len(self.map)):
        #   for j in range(len(self.map[i])):
        #      print(self.map[i][j])
        self.updatewindow()

    #Generates a new random map
    def newMap(self):
        print("NEW MAP!")
        self.map = MapCreator.mapGen(120, 160)[0]
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                (self.c.create_rectangle(5 * (i + 2), 5 * (j + 8), 5 * (i + 3), 5 * (j + 9),
                                         fill=self.colors[int(self.map[i][j])],
                                         outline='black'))

    #Handles click events from the mouse
    def mouseHandler(self, event):
        print("Clicked at:", event.x, event.y)
        if 10 < event.x < 610:
            if 40 < event.y < 840:
                x = int(((event.x - (event.x % 5))-10)/5)
                y = int(((event.y - (event.y % 5))-40)/5)
                print(self.map[x][y])
                self.labelGText.set(("G Value:", self.map[x][y]))
                self.labelHText.set(("H Value:", self.map[x][y]))
                self.labelFText.set(("F Value:", self.map[x][y]))
    def getAstar(self):
        self.updatewindow()
        print(self.start,self.end)
        path = astarSearch.a_star(self.map, (self.start[0],self.start[1]),(self.end[0],self.end[1]),120,160)
        print(path)
        for i in path[0]:
            print(i[0],i[1])
            (self.c.create_rectangle(5 * (i[0] + 2), 5 * (i[1] + 8), 5 * (i[0] + 3), 5 * (i[1] + 9),
            fill="Pink",
            outline='black'))
    def getWeightedAstar(self):
        self.updatewindow()
        getWeight1 = (self.weightedastar.get("1.0", "end"))
        getWeight1 = getdouble(getWeight1.strip())
        print(self.start,self.end)
        path = astarSearch.weighted_a_star(self.map, (self.start[0],self.start[1]),(self.end[0],self.end[1]),getWeight1,120,160)#Add UI Element Later
        print(path)
        for i in path[0]:
            print(i[0],i[1])
            (self.c.create_rectangle(5 * (i[0] + 2), 5 * (i[1] + 8), 5 * (i[0] + 3), 5 * (i[1] + 9),
            fill="Pink",
            outline='black'))
    def getSequentialHeuristic(self):
        self.updatewindow()
        getWeight1 = (self.heuristic1.get("1.0", "end"))
        getWeight1 = getdouble(getWeight1.strip())
        getWeight2 = (self.heuristic2.get("1.0", "end"))
        getWeight2 = getdouble(getWeight2.strip())
        print(self.start,self.end)
        path = astarSearch.sequential_heuristic(self.map, (self.start[0],self.start[1]),(self.end[0],self.end[1]),getWeight1,getWeight2,120,160)
        print(path)
        for i in path[0]:
            print(i[0],i[1])
            (self.c.create_rectangle(5 * (i[0] + 2), 5 * (i[1] + 8), 5 * (i[0] + 3), 5 * (i[1] + 9),
            fill="Pink",
            outline='black'))
    def getUniformCost(self):
        self.updatewindow()
        print(self.start,self.end)
        path = astarSearch.uniform_cost_search(self.map, (self.start[0],self.start[1]),(self.end[0],self.end[1]),120,160)
        print(path)
        for i in path[0]:
            print(i[0],i[1])
            (self.c.create_rectangle(5 * (i[0] + 2), 5 * (i[1] + 8), 5 * (i[0] + 3), 5 * (i[1] + 9),
            fill="Pink",
            outline='black'))
