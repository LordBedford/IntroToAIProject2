import math
from sys import maxsize
import MapCreator

class Node(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def battle(node, child):
    if node.value == 4:
        if child.value == 0:
            return 1
        elif child.value == 1:
            return 0
        elif child.value == 2:
            return 2
        elif child.value == 3:
            return -1
        elif child.value == 7:
            return -1
        else:
            return -2
    elif node.value == 5:
        if child.value == 0:
            return 1
        elif child.value == 1:
            return -1
        elif child.value == 2:
            return 0
        elif child.value == 3:
            return 2
        elif child.value == 7:
            return -1
        else:
            return -2
    else:
        if child.value == 0:
            return 1
        elif child.value == 1:
            return 2
        elif child.value == 2:
            return -1
        elif child.value == 3:
            return 0
        elif child.value == 7:
            return -1
        else:
            return -2

def sort_neighbors(map, node, temp):
    list = []
    for i in range(len(temp)):
        if temp[i][0] >= len(map) or temp[i][1] >= len(map[0]) or temp[i][0] < 0 or temp[i][1] < 0:
            continue
        child = Node(temp[i][0], temp[i][1], map[temp[i][0]][temp[i][1]])
        list.append( ( (temp[i][0], temp[i][1]), battle(node, child) ) )

    list.sort(key = lambda x: x[1])

    for i in range(len(list)):
        list[i] = list[i][0]

    return list

def takeTurn(map):
    scores = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
                node = Node(i,j, map[i][j])
                scores.append(MiniMax(map, node, node, 9, 1, 0,0))  # This begins the min max search with alpha beta pruning
    return (scores)

def MiniMax(map, node, child, depth, playerNum, a, b):

        #Get coordinates of all neighbors surrouding current node
        neighbors_temp = [(child.x-1, child.y), (child.x+1, child.y), (child.x, child.y-1), (child.x, child.y+1), 
        (child.x-1, child.y+1), (child.x-1, child.y-1), (child.x+1, child.y+1), (child.x+1, child.y-1)]

        neighbors = sort_neighbors(map, node, neighbors_temp)[::-1]

        if depth == 0:
            return battle(node,child), (node.x, node.y), (child.x, child.y)

        if playerNum > 0:
            val = -maxsize
            for i in range(len(neighbors)):
                child = Node(neighbors[i][0], neighbors[i][1], map[neighbors[i][0]][neighbors[i][1]])
                val = max(val, MiniMax(map, node, child, depth - 1, -playerNum, a, b)[0])
                a = max(a, val)
                if a >= b:
                    break
            return val, (node.x, node.y), (child.x, child.y)
        else:
            val = maxsize
            for i in range(len(neighbors)):
                child = Node(neighbors[i][0], neighbors[i][1], map[neighbors[i][0]][neighbors[i][1]])
                val = min(val, MiniMax(map, node, child, depth - 1, -playerNum, a, b)[0])
                b = min(b, val)
                if b <= a:
                    break
            return val, (node.x, node.y), (child.x, child.y)
#map = MapCreator.mapGen(9)
map = [
    [2,2,2],
    [0,0,0],
    [1,0,6]
]
print(takeTurn(map))