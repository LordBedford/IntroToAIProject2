#Peter Marchese

import random
from copy import copy, deepcopy

def getCoordinates(map):
    #Get start and end coordinates.
    start_x_cord = 0
    start_y_cord = 0
    end_x_cord = 0
    end_y_cord = 0
    while 1:
        while 1:
            rand = random.randint(1,4)
            if rand == 1:
                start_x_cord = random.randint(0,120-1)
                start_y_cord = random.randint(0,20)
                if map[start_x_cord][start_y_cord] != '0':
                    break
            elif rand == 2:
                start_x_cord = random.randint(0,20)
                start_y_cord = random.randint(0,160-1)
                if map[start_x_cord][start_y_cord] != '0':
                    break
            elif rand == 3:
                start_x_cord = random.randint(0,120-1)
                start_y_cord = random.randint(160-21,160-1)
                if map[start_x_cord][start_y_cord] != '0':
                    break
            else:
                start_x_cord = random.randint(120-21,120-1)
                start_y_cord = random.randint(0,160-1)
                if map[start_x_cord][start_y_cord] != '0':
                    break
        while 1:
            rand = random.randint(1,4)
            if rand == 1:
                end_x_cord = random.randint(0,120-1)
                end_y_cord = random.randint(0,20)
                if map[end_x_cord][end_y_cord] != '0':
                    break
            elif rand == 2:
                end_x_cord = random.randint(0,20)
                end_y_cord = random.randint(0,160-1)
                if map[end_x_cord][end_y_cord] != '0':
                    break
            elif rand == 3:
                end_x_cord = random.randint(0,120-1)
                end_y_cord = random.randint(160-21,160-1)
                if map[end_x_cord][end_y_cord] != '0':
                    break
            else:
                end_x_cord = random.randint(120-21,120-1)
                end_y_cord = random.randint(0,160-1)
                if map[end_x_cord][end_y_cord] != '0':
                    break
        if abs(start_x_cord - end_x_cord) > 100 or abs(start_y_cord - end_y_cord) > 100:
            #map[start_x_cord][start_y_cord] = '5'
            #map[end_x_cord][end_y_cord] = '6'
            break
    return start_x_cord, start_y_cord, end_x_cord, end_y_cord

#Function to generate a map
def mapGen(rows,cols):
    #Initiate map with all 1 chars for regular unblocked cell
    map = [['1' for i in range(cols)] for j in range(rows)]
    HTTList = []

    for i in range(8):
        #Get coordinates for hard to traverse terrain area
        x_cord = random.randint(0,rows-1)
        y_cord = random.randint(0,cols-1)

        HTTList.append( (x_cord,y_cord) )

        #Get range for the 31x31 area surrounding the coordinate. Fixes out of bounds errors
        row_start = x_cord - 15
        if x_cord-15 < 0:
            row_start = 0

        row_end = x_cord + 15
        if x_cord+15 > rows-1:
            row_end = rows-1

        col_start = y_cord - 15
        if y_cord-15 < 0:
            col_start = 0

        col_end = y_cord + 15
        if y_cord+15 > cols-1:
            col_end = cols-1

        #Fills in hard to traverse area
        for i in range(row_start, row_end+1):
            for j in range(col_start, col_end+1):
                if random.randint(1,2) == 1:
                    map[i][j] = '2'
    #Create rivers/highways
    #Get coordinates for river
    rivers = 0
    limit = 0
    while rivers < 4 and limit < 300:
        tempMap = deepcopy(map)
        river_x_cord = 0
        river_y_cord = 0
        #Determine what boundary river will start on
        #1 if on x-axis, 2 if on y-axis
        if random.randint(1,2) == 1:
            #top or bottom
            if random.randint(1,2) == 1:
                river_x_cord = rows-1
                river_y_cord = random.randint(0,cols-1)
            else: 
                river_x_cord = 0
                river_y_cord = random.randint(0,cols-1)
        else:
            #left or right
            if random.randint(1,2) == 1:
                river_y_cord = cols-1
                river_x_cord = random.randint(0,rows-1)
            else: 
                river_y_cord = 0
                river_x_cord = random.randint(0,rows-1)
        #Gets direction river will initially flow
        direction = ""
        if river_x_cord == rows-1:
            direction = "up"
        elif river_x_cord == 0:
            direction = "down"
        elif river_y_cord == cols-1:
            direction = "left"
        else: 
            direction = "right"

        tempxcord = river_x_cord
        tempycord = river_y_cord

        river_length = 0

        #Fill in river
        atBorder = 1
        hit_river = 0
        while atBorder:
            #Traverse 20 spaces
            counter = 0
            for j in range(20):
                #Up direction
                if direction == "up":
                    if tempxcord - j < 0:
                        atBorder = 0
                        break
                    counter += 1
                    if tempMap[tempxcord-j][tempycord] == '3' or tempMap[tempxcord-j][tempycord] == '4':
                        hit_river = 1
                    #Check if hard to traverse terrain
                    if tempMap[tempxcord - j][tempycord] == '1':
                        tempMap[tempxcord - j][tempycord] = '3'
                        river_length += 1
                    elif tempMap[tempxcord - j][tempycord] == '2':
                        tempMap[tempxcord - j][tempycord] = '4'
                        river_length += 1
                #Down direction
                if direction == "down":
                    if tempxcord + j > rows-1:
                        atBorder = 0
                        break
                    counter += 1
                    if tempMap[tempxcord+j][tempycord] == '3' or tempMap[tempxcord+j][tempycord] == '4':
                        hit_river = 1
                    #Check if hard to traverse terrain
                    if tempMap[tempxcord + j][tempycord] == '1':
                        tempMap[tempxcord + j][tempycord] = '3'
                        river_length += 1
                    elif tempMap[tempxcord + j][tempycord] == '2':
                        tempMap[tempxcord + j][tempycord] = '4'
                        river_length += 1
                # #Left direction
                if direction == "left":
                    if tempycord - j < 0:
                        atBorder = 0
                        break
                    counter += 1
                    if tempMap[tempxcord][tempycord-j] == '3' or tempMap[tempxcord][tempycord-j] == '4':
                        hit_river = 1
                    #Check if hard to traverse terrain 
                    if tempMap[tempxcord][tempycord - j] == '1':
                        tempMap[tempxcord][tempycord - j] = '3'
                        river_length += 1
                    elif tempMap[tempxcord][tempycord - j] == '2':
                        tempMap[tempxcord][tempycord - j] = '4'
                        river_length += 1
                #Right direction
                if direction == "right":
                    if tempycord + j > cols-1:
                        atBorder = 0
                        break
                    counter += 1
                    if tempMap[tempxcord][tempycord+j] == '3' or tempMap[tempxcord][tempycord+j] == '4':
                        hit_river = 1
                    #Check if hard to traverse terrain
                    if tempMap[tempxcord][tempycord + j] == '1':
                        tempMap[tempxcord][tempycord + j] = '3'
                        river_length += 1
                    elif tempMap[tempxcord][tempycord + j] == '2':
                        tempMap[tempxcord][tempycord + j] = '4'
                        river_length += 1
            #Gets coordinates for current position of river
            #Roll for new direction and change coordinates and path accordingly
            rand = random.randint(1,5)
            if direction == "up":
                tempxcord -= counter
                if rand == 1:
                    direction = "left"
                elif rand == 2:
                    direction = "right"
            elif direction == "down":
                tempxcord += counter
                if rand == 1:
                    direction = "left"
                elif rand == 2:
                    direction = "right"
            elif direction == "left":
                tempycord -= counter
                if rand == 1:
                    direction = "up"
                elif rand == 2:
                    direction = "down"
            elif direction == "right":
                tempycord += counter
                if rand == 1:
                    direction = "up"
                elif rand == 2:
                    direction = "down"
            #Check if current position is out of bounds. If so, stop loop.
            if tempycord < 0 or tempycord > cols-1 or tempxcord < 0 or tempxcord > rows-1:
                atBorder = 0
        if river_length >= 100 and hit_river != 1 and atBorder == 0:
            rivers += 1
            map = deepcopy(tempMap)
        limit += 1
    #Add impassable terrain
    impassable_number = rows * cols / 5
    imp = 0
    while imp <= impassable_number:
        x_cord = random.randint(0,rows-1)
        y_cord = random.randint(0,cols-1)
        if map[x_cord][y_cord] != '3' and map[x_cord][y_cord] != '4' and map[x_cord][y_cord] != '0':
            map[x_cord][y_cord] = '0'
            imp += 1
    return map, HTTList
mapGen(120,160)