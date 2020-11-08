import math
from sys import maxsize
import MapCreator

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

# def takeTurn(map):
#     scores = []
#     for i in range(len(map)):
#         for j in range(len(map[i])):
#             if map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
#                 node = Node(i,j, map[i][j])
#                 scores.append(MiniMax(map, node, node, 9, 1, 0, 0))  # This begins the min max search with alpha beta pruning
#     return (scores)

def MiniMax(node, depth, playerNum, a, b):

        #Get coordinates of all neighbors surrouding current node
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1,-1), (1,1), (1,-1)]

        print(Evaluate(node.board, GetBoardEvals(node.board), playerNum))

        if depth == 0:
            return node.value
        if playerNum > 0:
            val = -maxsize
            for i in range(len(node.board)):
                for j in range(len(node.board[i])):
                    if node.board[i][j] in [4,5,6]:
                        for n in neighbors:
                            if i+n[0] >= len(node.board) or j+n[1] >= len(node.board[0]) or i+n[1] < 0 or j+n[1] < 0:
                                continue
                            child = Node(node.board, node.value)
                            temp = child.board[i][j]
                            child.board[i][j] = child.board[i+n[0]][j+n[1]]
                            child.board[i+n[0]][j+n[1]] = temp

                            child.value = Evaluate(child.board, GetBoardEvals(child.board), playerNum)

                            val = max(val, MiniMax(child, depth - 1, -playerNum, a, b))
                            a = max(a, val)
                            if a >= b:
                                break
            return val 
        else:
            val = maxsize
            for i in range(len(node.board)):
                for j in range(len(node.board[i])):
                    if node.board[i][j] in [1,2,3]:
                        for n in neighbors:
                            if i+n[0] >= len(node.board) or j+n[1] >= len(node.board[0]) or i+n[1] < 0 or j+n[1] < 0:
                                continue
                            child = Node(node.board, -node.value)
                            temp = child.board[i][j]
                            child.board[i][j] = child.board[i+n[0]][j+n[1]]
                            child.board[i+n[0]][j+n[1]] = temp

                            child.value = Evaluate(child.board, GetBoardEvals(child.board), playerNum)

                            val = min(val, MiniMax(child, depth - 1, -playerNum, a, b))
                            b = min(a, val)
                            if b <= a:
                                break
            return val
#map = MapCreator.mapGen(9)
map = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [7,7,0,0,0,0],
    [1,0,6,0,0,0]
]
node = Node(map, 1)
print(MiniMax(node, 3, 1, -math.inf, math.inf))