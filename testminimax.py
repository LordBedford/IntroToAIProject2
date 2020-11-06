import math
from sys import maxsize


def takeTurn(map):
    pieces = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
                pieces.append((i, j))
    return findMax(map, pieces, 0, -math.inf, math.inf)  # This begins the min max search with alpha beta pruning


def findMax(map, pieces, depth, alpha, beta):
    value = -math.inf
    tempPieces = list(pieces)
    retMap = []
    value = 0
    if depth == 3:
        return [Evaluate(map), map]
    else:
        for i in pieces:
                tempMap = []
                temp =[]
                if testIfPossible(map, i[0], i[1], i[0] + 1, i[1]):
                    tempMap.append(simulateMove(map, i[0], i[1], i[0] + 1, i[1]))
                    if tempMap[0][1]:
                        tempPieces.remove(i)
                    temp = list(findMin(tempMap[0][0], pieces, depth + 1, alpha, beta))
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap = list(tempMap[0][0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces)
                tempMap = []
                if testIfPossible(map, i[0], i[1], i[0] - 1, i[1]):
                    tempMap.append(simulateMove(map, i[0], i[1], i[0] - 1, i[1]))
                    if tempMap[0][1]:
                        tempPieces.remove(i)
                    temp = findMin(tempMap[0][0], pieces, depth + 1, alpha, beta)
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap = list(tempMap[0][0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces[0])
                tempMap = []
                if testIfPossible(map, i[0], i[1], i[0], i[1] + 1):
                    tempMap.append(simulateMove(map, i[0], i[1], i[0], i[1] + 1))
                    if tempMap[0][1]:
                        tempPieces.remove(i)
                    temp = list(findMin(tempMap[0][0], pieces, depth + 1, alpha, beta))
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap = list(tempMap[0][0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces)
                tempMap = []
                if testIfPossible(map, i[0], i[1], i[0], i[1] - 1):
                    tempMap.append(simulateMove(map, i[0], i[1], i[0], i[1] - 1))
                    if tempMap[0][1]:
                        tempPieces.remove(i)
                    temp = list(findMin(tempMap[0][0], pieces, depth + 1, alpha, beta))
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap = list(tempMap[0][0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces)
        return [value, retMap]


def findMin(map, pieces, depth, alpha, beta):
    value = math.inf
    tempPieces = list(pieces)
    retMap = []
    if depth == 3:
        return [Evaluate(map), map]
    else:
        for i in pieces:
            tempMap = []
            temp =[]
            if testIfPossible(map, i[0], i[1], i[0] + 1, i[1]):
                tempMap.append(simulateMove(map, i[0], i[1], i[0] + 1, i[1]))
                if tempMap[0][1]:
                    tempPieces.remove(i)
                temp = list(findMax(tempMap[0][0], pieces, depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] < value:
                    value = temp[0]
                    retMap = list(tempMap[0][0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)
            tempMap = []
            if testIfPossible(map, i[0], i[1], i[0] - 1, i[1]):
                tempMap.append(simulateMove(map, i[0], i[1], i[0] - 1, i[1]))
                if tempMap[0][1]:
                    tempPieces.remove(i)
                temp = list(findMax(tempMap[0][0], pieces, depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] < value:
                    value = temp[0]
                    retMap = list(tempMap[0][0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)
            tempMap = []
            if testIfPossible(map, i[0], i[1], i[0], i[1] + 1):
                tempMap.append(simulateMove(map, i[0], i[1], i[0], i[1] + 1))
                if tempMap[0][1]:
                    tempPieces.remove((i[0],i[1]))
                temp = list(findMax(tempMap[0][0], pieces, depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] < value:
                    value = temp[0]
                    retMap = list(tempMap[0][0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)
            tempMap = []
            if testIfPossible(map, i[0], i[1], i[0], i[1] - 1):
                tempMap.append(simulateMove(map, i[0], i[1], i[0], i[1] - 1))
                if tempMap[0][1]:
                    tempPieces.remove(i)
                temp = list(findMax(tempMap[0][0], pieces, depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] > value:
                    value = temp[0]
                    retMap = list(tempMap[0][0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)

        return [value, retMap]


def testIfPossible(map, y1, x1, y2, x2):
    if y2 >= len(map) or x2 >= len(map[y2]) or y2 < 0 or x2 < 0:
        return False
    elif map[y2][x2] == 4 or map[y2][x2] == 5 or map[y2][x2] == 6:
        return False
    elif (-1 <= (x1 - x2) <= 1) and (-1 <= (y1 - y2) <= 1):
        return True
    else:
        return False


def simulateMove(map, x1, y1, x2, y2):
    if map[x2][y2] == 0:
        return moveOnToGrass(map, x1, y1, x2, y2)
    elif map[x2][y2] == 7:
        return moveOnToPit(map, x1, y1, x2, y2)
    elif map[x2][y2] == 1 or map[x2][y2] == 2 or map[x2][y2] == 3:
        return combat(map, x1, y1, x2, y2)


# Move/combat methods return map and true/false if true the piece is removed from pieces on return.

def moveOnToGrass(map, x1, y1, x2, y2):
    map[y2][x2] = map[y1][x1]
    map[y1][x1] = 0
    return [map, False]


def moveOnToPit(map, x1, y1, x2, y2):
    map[x1][y1] = 0
    return [map, True]


def combat(map, x1, y1, x2, y2):
    if map[x1][y1] == map[x2][y2] - 3:  # Are the pieces the same?
        map[x1][y1] = 0
        map[x2][y2] = 0
        return [map, True]
    elif map[x1][y1] == 4:  # is the AI piece a hero?
        if map[x2][y2] == 2:
            map[x2][y2] = map[x1][y1]
            map[x1][y1] = 0
            return [map, False]
        elif map[x2][y2] == 3:
            map[x1][y1] = 0
            return [map, True]
    elif map[x1][y1] == 5:  # is the AI piece a Wumpus?
        if map[x2][y2] == 3:
            map[x2][y2] = map[x1][y1]
            map[x1][y1] = 0
            return [map, False]
        elif map[x2][y2] == 1:
            map[x1][y1] = 0
            return [map, True]
    elif map[x1][y1] == 5:  # is the AI piece a Wizard?
        if map[x2][y2] == 1:
            map[x2][y2] = map[x1][y1]
            map[x1][y1] = 0
            return [map, False]
        elif map[x2][y2] == 2:
            map[x1][y1] = 0
            return [map, True]


def Evaluate(map):
    aiCount = 0
    playerCount = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1 or map[i][j] == 2 or map[i][j] == 3:
                playerCount = playerCount + 1
            elif map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
                aiCount = aiCount + 1
    return playerCount - aiCount
