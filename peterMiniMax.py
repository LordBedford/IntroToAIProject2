import math
from sys import maxsize
import MapCreator
from copy import copy,deepcopy

class Node(object):
    def __init__(self, board, value):
        self.board = board
        self.value = value

def Evaluate(board, eboard, playerNum):
    aiCount = 0
    playerCount = 0
    aiBoardValue = 0
    playerBoardValue = 0
    value = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3):
                aiCount = aiCount + 10
                aiBoardValue = eboard[i][j]
                aiCount = aiCount + aiBoardValue
            elif (board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6):
                playerCount = playerCount + 10
                playerBoardValue = eboard[i][j]
                playerCount = playerCount + playerBoardValue
    return playerCount - aiCount

def GetBoardEvals(board):
    eboard = [[0 for i in range(len(board))] for j in range(len(board))]
    center = len(board) // 2
    # assign higher values for centralized cells
    for i in range(len(board)):
        for j in range(len(board)):
            eboard[i][j] = 0
    if len(board) == 3:
        eboard[center][center] = 2
    if len(board) == 6:
        eboard[center][center] = 2
        eboard[center + 1][center] = 2
        eboard[center + 1][center + 1] = 2
        eboard[center][center + 1] = 2
    if len(board) == 9:
        eboard[center][center] = 2
        eboard[center + 1][center] = 2
        eboard[center + 1][center + 1] = 2
        eboard[center][center + 1] = 2
        eboard[center + 2][center] = 2
        eboard[center + 2][center + 1] = 2
        eboard[center + 2][center + 2] = 2
        eboard[center][center + 2] = 2
        eboard[center + 1][center + 2] = 2

    # if pit, assign value of -10
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 7:
                eboard[i][j] = -10
    return eboard

def makeMove(node, i,j, k,f):
    if node.board[k][f] == 0:
        node.board[k][f] = node.board[i][j]
        node.board[i][j] = 0
        return node.board
    if node.board[k][f] == 7:
        node.board[i][j] == 0
        return node.board
    #Player Hero
    if node.board[i][j] == 1:
        if node.board[k][f] == 5:
            node.board[i][j] = 0
            node.board[k][f] = 1
            return node.board
        elif node.board[k][f] == 4:
            node.board[i][j] == 0
            node.board[k][f] == 0
            return node.board
        elif node.board == 6:
            node.board[i][j] == 0
            node.board[k][f] == 6
            return node.board
    #Player Wumpus
    if node.board[i][j] == 2:
        if node.board[k][f] == 5:
            node.board[i][j] = 0
            node.board[k][f] = 0
            return node.board
        elif node.board[k][f] == 4:
            node.board[i][j] == 0
            node.board[k][f] == 4
            return node.board
        elif node.board == 6:
            node.board[i][j] == 2
            node.board[k][f] == 0
            return node.board
    #Player Mage
    if node.board[i][j] == 3:
        if node.board[k][f] == 5:
            node.board[i][j] = 0
            node.board[k][f] = 5
            return node.board
        elif node.board[k][f] == 4:
            node.board[i][j] == 3
            node.board[k][f] == 0
            return node.board
        elif node.board == 6:
            node.board[i][j] == 0
            node.board[k][f] == 0
            return node.board
    #AI Hero
    if node.board[i][j] == 4:
        if node.board[k][f] == 1:
            node.board[i][j] = 0
            node.board[k][f] = 0
            return node.board
        elif node.board[k][f] == 2:
            node.board[i][j] == 0
            node.board[k][f] == 4
            return node.board
        elif node.board == 3:
            node.board[i][j] == 0
            node.board[k][f] == 3
            return node.board
    #AI Wumpus
    if node.board[i][j] == 5:
        if node.board[k][f] == 1:
            node.board[i][j] = 0
            node.board[k][f] = 1
            return node.board
        elif node.board[k][f] == 2:
            node.board[i][j] == 0
            node.board[k][f] == 0
            return node.board
        elif node.board == 3:
            node.board[i][j] == 0
            node.board[k][f] == 5
            return node.board
    #AI Mage
    if node.board[i][j] == 6:
        if node.board[k][f] == 1:
            node.board[i][j] = 0
            node.board[k][f] = 6
            return node.board
        elif node.board[k][f] == 2:
            node.board[i][j] == 0
            node.board[k][f] == 2
            return node.board
        elif node.board == 3:
            node.board[i][j] == 0
            node.board[k][f] == 0
            return node.board
    #return node.board

def MiniMax(node, depth, playerNum, a, b):

        #Get coordinates of all neighbors surrouding current node
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1,-1), (1,1), (1,-1)]
        children = []

        if depth == 0:
            return node.value, node.board
        if playerNum > 0:  
            val = -maxsize
            for i in range(len(node.board)):
                for j in range(len(node.board[i])):
                    if node.board[i][j] in [4,5,6]:
                        for n in neighbors:
                            if i+n[0] >= len(node.board) or j+n[1] >= len(node.board[0]) or i+n[0] < 0 or j+n[1] < 0:
                                continue
                            child = deepcopy(node) 
                            child.board = makeMove(child, i,j, i+n[0], j+n[1])
                            if child.board == None:
                                continue
                            child.value = Evaluate(child.board, GetBoardEvals(child.board), playerNum)
                            children.append(child)
            mapper = None
            for x in children:
                temp = MiniMax(x, depth - 1, -playerNum, a, b)
                if val < temp[0]:
                    mapper = temp[1]
                val = max(val, temp[0])
                a = max(a, val)
                if a >= b:
                    break
            return val, mapper
        else:
            val = maxsize
            for i in range(len(node.board)):
                for j in range(len(node.board[i])):
                    if node.board[i][j] in [1,2,3]:
                        for n in neighbors:
                            if i+n[0] >= len(node.board) or j+n[1] >= len(node.board[0]) or i+n[0] < 0 or j+n[1] < 0:
                                continue
                            child = deepcopy(node) 
                            child.board = makeMove(child, i,j, i+n[0], j+n[1])
                            if child.board == None:
                                continue
                            child.value = -Evaluate(child.board, GetBoardEvals(child.board), playerNum)
                            children.append(child)
            mapper = None
            for x in children:
                temp = MiniMax(x, depth - 1, -playerNum, a, b)
                if val > temp[0]:
                    mapper = temp[1]
                val = min(val, temp[0])
                b = min(a, val)
                if b <= a:
                    break
            return val, mapper
#map = MapCreator.mapGen(9)
map = [
    [0,0,2,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [7,7,0,0,0,0],
    [1,0,6,0,0,0]
]
node = Node(map, Evaluate(map, GetBoardEvals(map),1))
thing = MiniMax(node, 20, 1, -math.inf, math.inf)
print(thing[0])
print(thing[1])