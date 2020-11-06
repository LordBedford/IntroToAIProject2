import math
from sys import maxsize

def takeTurn(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 4 or map[i][j] == 5 or map[i][j] == 6:
                return MiniMax(map, map[i][j], 9, 1, -math.inf, math.inf)  # This begins the min max search with alpha beta pruning

def MiniMax(map, node, depth, playerNum, a, b):
        if depth == 0 or abs(node.value) == maxsize:
            return node.value
        if playerNum > 0:
            bestValue = maxsize * playerNum
            for i in range(len(node.children)):
                child = node.children[i]
                val = MiniMax(child, depth - 1, -playerNum, a, b)
                if abs(maxsize * playerNum - val) < abs(maxsize * playerNum - bestValue):
                    bestValue = val
                a = max(a, bestValue)
                if a >= b:
                    break
            return bestValue
        else:
            bestValue = maxsize * playerNum
            for i in range(len(node.children)):
                child = node.children[i]
                val = MiniMax(child, depth - 1, -playerNum, a ,b)
                if abs(maxsize * playerNum - val) < abs(maxsize * playerNum - bestValue):
                    bestValue = val
                b = min(b, bestValue)
                if b <= a:
                    break
            return bestValue