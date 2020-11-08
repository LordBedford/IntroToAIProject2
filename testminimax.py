import math
from sys import maxsize


def takeTurn(map):
    pieces = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
                pieces.append((i, j))
    return findMax(map,  0, -math.inf, math.inf)  # This begins the min max search with alpha beta pruning


def findMax(map,  depth, alpha, beta):
    pieces = getAIPieces(map)
    value = -math.inf
    tempPieces = list(pieces)
    retMap = []
    value = -math.inf
    if depth == 3:
        return [Evaluate(map), map]
    else:
        for i in pieces:
                tempMap = []
                temp =[]
                if testIfPossible(map, i[0], i[1], i[0] + 1, i[1]):
                    tempMap =(simulateMove(map, i[0], i[1], i[0] + 1, i[1]))
                   
                    temp =(findMin(tempMap[0],  depth + 1, alpha, beta))
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap =(tempMap[0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces)
                if testIfPossible(map, i[0], i[1], i[0] - 1, i[1]):
                    tempMap = []
                    temp = []
                    tempMap = simulateMove(map, i[0], i[1], i[0] - 1, i[1])
                    temp = findMin(tempMap[0],  depth + 1, alpha, beta)
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap =(tempMap[0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces[0])
                if testIfPossible(map, i[0], i[1], i[0], i[1] + 1):
                    tempMap = []
                    temp = []
                    tempMap =(simulateMove(map, i[0], i[1], i[0], i[1] + 1))
                   
                    temp =(findMin(tempMap[0],  depth + 1, alpha, beta))
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap =(tempMap[0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces)

                if testIfPossible(map, i[0], i[1], i[0], i[1] - 1):
                    tempMap = []
                    temp = []
                    tempMap =(simulateMove(map, i[0], i[1], i[0], i[1] - 1))
                   
                    temp =(findMin(tempMap[0],  depth + 1, alpha, beta))
                    if temp[0] > alpha:
                        alpha = temp[0]
                    if temp[0] > value:
                        value = temp[0]
                        retMap =(tempMap[0])
                    if alpha > beta:
                        return [value, retMap]
                    tempPieces = list(pieces)
        return [value, retMap]


def findMin(map,  depth, alpha, beta):
    pieces = getAIPieces(map)
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
                tempMap = simulateMove(map, i[0], i[1], i[0] + 1, i[1])
               
                temp = findMax(tempMap[0],  depth + 1, alpha, beta)
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] < value:
                    value = temp[0]
                    retMap =(tempMap[0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)
            if testIfPossible(map, i[0], i[1], i[0] - 1, i[1]):
                tempMap = []
                temp = []
                tempMap = simulateMove(map, i[0], i[1], i[0] - 1, i[1])
               
                temp =(findMax(tempMap[0],  depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] < value:
                    value = temp[0]
                    retMap =(tempMap[0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)
            if testIfPossible(map, i[0], i[1], i[0], i[1] + 1):
                tempMap = []
                temp = []
                tempMap = simulateMove(map, i[0], i[1], i[0], i[1] + 1)
                if tempMap[1]:
                    tempPieces.remove((i[0],i[1]))
                temp =(findMax(tempMap[0],  depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] < value:
                    value = temp[0]
                    retMap =(tempMap[0])
                if alpha > beta:
                    return [value, retMap]
                tempPieces = list(pieces)
            if testIfPossible(map, i[0], i[1], i[0], i[1] - 1):
                tempMap = []
                temp = []
                tempMap =(simulateMove(map, i[0], i[1], i[0], i[1] - 1))
               
                temp =(findMax(tempMap[0],  depth + 1, alpha, beta))
                if temp[0] < beta:
                    beta = temp[0]
                if temp[0] > value:
                    value = temp[0]
                    retMap =(tempMap[0])
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


def simulateMove(map, y1, x1, y2, x2):
    tempMap = []
    for i in range(len(map)):
        holder = []
        for j in range(len(map[i])):
           holder.append(map[i][j])
        tempMap.append(holder)
    if tempMap[y2][x2] == 0:
        return moveOnToGrass(tempMap, y1, x1, y2, x2)
    elif tempMap[y2][x2] == 7:
        return moveOnToPit(tempMap, y1, x1, y2, x2)
    elif tempMap[y2][x2] == 1 or tempMap[y2][x2] == 2 or tempMap[x2][y2] == 3:
        return combat(tempMap, y1, x1, y2, x2)
    else:
        print("Fucked")
        print(map)
        print(map[x1][y1])
        print(map[x2][y2])


# Move/combat methods return map and true/false if true the piece is removed from pieces on return.

def moveOnToGrass(map, x1, y1, x2, y2):
    map[y2][x2] = map[y1][x1]
    map[y1][x1] = 0
    ret = [map, False]
    return ret


def moveOnToPit(map, x1, y1, x2, y2):
    map[x1][y1] = 0
    return [map, True]


def combat(map, y1, x1, y2, x2):
    if map[y1][x1] == 0:
        print("WTF")
    if map[y1][x1] - 3 == map[y2][x2]:  # Are the pieces the same?
        map[y1][x1] = 0
        map[y2][x2] = 0
        ret = [map, True]
        return ret
    elif map[y1][x1] == 4:  # is the AI piece a hero?
        if map[y2][x2] == 2:
            map[y2][x2] = map[x1][y1]
            map[y1][x1] = 0
            return [map, False]
        elif map[y2][x2] == 3:
            map[y1][x1] = 0
            return [map, True]
    elif map[y1][x1] == 5:  # is the AI piece a Wumpus?
        if map[y2][x2] == 3:
            map[y2][x2] = map[x1][y1]
            map[y1][x1] = 0
            return [map, False]
        elif map[y2][x2] == 1:
            map[y1][x1] = 0
            return [map, True]
    elif map[y1][x1] == 6:  # is the AI piece a Wizard?
        if map[y2][x2] == 1:
            map[y2][x2] = map[x1][y1]
            map[y1][x1] = 0
            return [map, False]
        elif map[y2][x2] == 2:
            map[y1][x1] = 0
            return [map, True]
    else:
        print("UBER FUCKED")


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

def getAIPieces(map):
    aiCount = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
                aiCount.append((i,j))
    return aiCount