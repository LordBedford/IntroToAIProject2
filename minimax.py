# Brian Tran
from sys import maxsize
import copy

class Node(object):
    def __init__(self, depth, playerNum, board, value):
        self.depth = depth
        self.playerNum = playerNum  # negative playerNum = AI agent
        self.board = board
        self.eboard = GetBoardEvals(board)
        self.value = Evaluate(board, self.eboard, playerNum)
        self.children = CreateChildren(self, depth, board, playerNum)

def CreateChildren(self, depth, board, playerNum):
    children = []
    copyList = []
    if depth > 0:
        eboard = GetBoardEvals(board)
        tempBoard = board
        validChildren = []
        for i in range(len(board)):
            for j in range(len(board)):
                # AI agent's turn (4->2, 6->1, 5->3)
                if (playerNum < 0):
                    if (board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6):
                        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i + 1, j - 1),
                                     (i - 1, j + 1),
                                     (i - 1, j - 1)]
                        for next in neighbors:
                            # Checks to see if neighbors are within Bounds
                            if next[0] < 0 or \
                                    next[1] < 0 or \
                                    next[0] >= len(board) or \
                                    next[1] >= len(board):
                                continue
                            validChildren.append(next)
                        if (board[i][j] == 4):
                            tempBoard = board
                            # Checks to see if neighbors can kill units
                            for next in validChildren:

                                oldVal = tempBoard[next[0]][next[1]]
                                otherVal = tempBoard[i][j]


                                # Heros can't kill mage
                                if board[next[0]][next[1]] == 3:
                                    continue
                                # Hero kills wumpus
                                if board[next[0]][next[1]] == 2:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 4
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Heros Tie and kill each other
                                if board[next[0]][next[1]] == 1:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 0
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Open Space
                                else:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 4
                                    tempBoard[i][j] = 0

                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # I NEED TO RESET THE BOARD BACK BUT IT ADDS THE RESETTED BOARD TO THE LIST???

                                board[next[0]][next[1]] = oldVal
                                board[i][j] = otherVal



                        if (board[i][j] == 5):
                            # Checks to see if neighbors can kill units
                            for next in validChildren:

                                oldVal = tempBoard[next[0]][next[1]]
                                otherVal = tempBoard[i][j]

                                # Wumpus can't kill hero
                                if board[next[0]][next[1]] == 1:
                                    continue
                                # Wumps kills mage
                                if board[next[0]][next[1]] == 3:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 5
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Wumpus Tie and kill each other
                                if board[next[0]][next[1]] == 2:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 0
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)


                                # Open Space
                                else:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 5
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                board[next[0]][next[1]] = oldVal
                                board[i][j] = otherVal

                        if (board[i][j] == 6):
                            # Checks to see if neighbors can kill units
                            for next in validChildren:

                                oldVal = tempBoard[next[0]][next[1]]
                                otherVal = tempBoard[i][j]

                                # Mage can't kill wumpus
                                if board[next[0]][next[1]] == 2:
                                    continue
                                # Mage kills hero
                                if board[next[0]][next[1]] == 1:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 6
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Mages Tie and kill each other
                                if board[next[0]][next[1]] == 3:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 0
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Open Space
                                else:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 6
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                board[next[0]][next[1]] = oldVal
                                board[i][j] = otherVal

                # Player's turn
                elif (playerNum > 0):
                    if (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3):
                        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i + 1, j - 1),
                                     (i - 1, j + 1),
                                     (i - 1, j - 1)]
                        for next in neighbors:
                            # Checks to see if neighbors are within Bounds
                            if next[0] < 0 or \
                                    next[1] < 0 or \
                                    next[0] >= len(board) or \
                                    next[1] >= len(board):
                                continue
                            validChildren.append(next)
                        if (board[i][j] == 1):
                            # Checks to see if neighbors can kill units
                            for next in validChildren:

                                oldVal = tempBoard[next[0]][next[1]]
                                otherVal = tempBoard[i][j]

                                # Heros can't kill mage
                                if board[next[0]][next[1]] == 6:
                                    continue
                                # Hero kills wumpus
                                if board[next[0]][next[1]] == 5:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 1
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Heros Tie and kill each other
                                if board[next[0]][next[1]] == 4:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 0
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Open Space
                                else:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 1
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                board[next[0]][next[1]] = oldVal
                                board[i][j] = otherVal

                        if (board[i][j] == 2):
                            # Checks to see if neighbors can kill units
                            for next in validChildren:

                                oldVal = tempBoard[next[0]][next[1]]
                                otherVal = tempBoard[i][j]

                                # Wumpus can't kill hero
                                if board[next[0]][next[1]] == 4:
                                    continue
                                # Wumps kills mage
                                if board[next[0]][next[1]] == 6:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 2
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Wumpus Tie and kill each other
                                if board[next[0]][next[1]] == 5:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 0
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Open Space
                                else:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 2
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                board[next[0]][next[1]] = oldVal
                                board[i][j] = otherVal

                        if (board[i][j] == 3):
                            # Checks to see if neighbors can kill units
                            for next in validChildren:

                                oldVal = tempBoard[next[0]][next[1]]
                                otherVal = tempBoard[i][j]

                                # Mage can't kill wumpus
                                if board[next[0]][next[1]] == 5:
                                    continue
                                # Mage kills hero
                                if board[next[0]][next[1]] == 4:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 3
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Mages Tie and kill each other
                                if board[next[0]][next[1]] == 6:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 0
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                # Open Space
                                else:
                                    tempBoard = board
                                    tempBoard[next[0]][next[1]] = 3
                                    tempBoard[i][j] = 0
                                    copyList = copy.deepcopy(tempBoard)
                                    curVal = Evaluate(copyList, eboard, playerNum)
                                    cur = Node(depth - 1, -playerNum, copyList, curVal)
                                    children.append(cur)

                                board[next[0]][next[1]] = oldVal
                                board[i][j] = otherVal

    #print("ALL CHILDREN BOARDS")
    #print(len(children))
    #for i in range(len(children)):
        #print(children[i].board)

    return children


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


# generates a general board evaluation based on the dimensions of the board
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

def GameOver(board):
    aiCount = 0
    playerCount = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3):
                playerCount = playerCount + 1
            if (board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6):
                aiCount = aiCount + 1
    if(aiCount == 0 or playerCount == 0):
        return True
    return False

def MiniMax(node, depth, playerNum, a, b):
    if (depth == 0) or GameOver(node.board):
        return node.value
    if (playerNum > 0):
        bestValue = maxsize
        for i in range(len(node.children)):
            child = node.children[i]
            bestValue = min(bestValue, MiniMax(child, depth - 1, -playerNum, a, b))
            #a = min(a, bestValue)
            #if (a <= b):
                #break
        return bestValue
    else:
        bestValue = -maxsize
        for i in range(len(node.children)):
            child = node.children[i]
            bestValue = max(bestValue, MiniMax(child, depth - 1, -playerNum, a, b))
            #b = max(b, bestValue)
            #if (b >= a):
                #break
        return bestValue



def GetNextMove(board, depth, playerNum):
    cur = Node(depth, playerNum, board, 0)
    print("ALL CHILDREN BOARDS")
    print(len(cur.children))
    for i in range(len(cur.children)):
        print(cur.children[i].board, cur.children[i].value)

    val = MiniMax(cur, depth, playerNum, 0, 0)


    print(val)
    return cur.board