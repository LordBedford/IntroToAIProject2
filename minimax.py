# Brian Tran
from sys import maxsize


class Node(object):
    def __init__(self, depth, playerNum, board, value):
        self.depth = depth
        self.playerNum = playerNum  # negative playerNum = AI agent
        self.children = []
        self.board = board
        self.eboard = GetBoardEvals(board)
        self.value = Evaluate(board, self.eboard, playerNum)
        self.CreateChildren(depth, board, playerNum)

    def CreateChildren(self, depth, board, playerNum):
        print("INITIAL BOARD")
        print(board)
        print("DEPTH")
        print(depth)
        print("PLAYER NUM:")
        print(playerNum)
        if depth >= 0:
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
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Heros Tie and kill each other
                                    if board[next[0]][next[1]] == 1:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Open Space
                                    else:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 4
                                        tempBoard[i][j] = 0
                                        newVal = 4

                                        copy = tempBoard
                                        curVal = Evaluate(copy, eboard, playerNum)
                                        cur = Node(depth - 1, -playerNum, copy, curVal)
                                        self.children.append(cur)
                                        print("JUST ADDED")
                                        print(self.children[0].board)

                                        print("CUR BOARD")
                                        print(self.children[0].board)

                                    #I NEED TO RESET THE BOARD BACK BUT IT ADDS THE RESETTED BOARD TO THE LIST???
                                    tempBoard[next[0]][next[1]] = oldVal
                                    tempBoard[i][j] = otherVal



                            if (board[i][j] == 5):
                                # Checks to see if neighbors can kill units
                                for next in validChildren:
                                    # Wumpus can't kill hero
                                    if board[next[0]][next[1]] == 1:
                                        continue
                                    # Wumps kills mage
                                    if board[next[0]][next[1]] == 3:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 5
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Wumpus Tie and kill each other
                                    if board[next[0]][next[1]] == 2:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Open Space
                                    else:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 5
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                            if (board[i][j] == 6):
                                # Checks to see if neighbors can kill units
                                for next in validChildren:
                                    # Mage can't kill wumpus
                                    if board[next[0]][next[1]] == 2:
                                        continue
                                    # Mage kills hero
                                    if board[next[0]][next[1]] == 1:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 6
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Mages Tie and kill each other
                                    if board[next[0]][next[1]] == 3:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Open Space
                                    else:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 6
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

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
                                    # Heros can't kill mage
                                    if board[next[0]][next[1]] == 6:
                                        continue
                                    # Hero kills wumpus
                                    if board[next[0]][next[1]] == 5:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 1
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Heros Tie and kill each other
                                    if board[next[0]][next[1]] == 4:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Open Space
                                    else:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 1
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                            if (board[i][j] == 2):
                                # Checks to see if neighbors can kill units
                                for next in validChildren:
                                    # Wumpus can't kill hero
                                    if board[next[0]][next[1]] == 4:
                                        continue
                                    # Wumps kills mage
                                    if board[next[0]][next[1]] == 6:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 2
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Wumpus Tie and kill each other
                                    if board[next[0]][next[1]] == 5:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Open Space
                                    else:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 2
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                            if (board[i][j] == 3):
                                # Checks to see if neighbors can kill units
                                for next in validChildren:
                                    # Mage can't kill wumpus
                                    if board[next[0]][next[1]] == 5:
                                        continue
                                    # Mage kills hero
                                    if board[next[0]][next[1]] == 4:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 3
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Mages Tie and kill each other
                                    if board[next[0]][next[1]] == 6:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

                                    # Open Space
                                    else:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 3
                                        tempBoard[i][j] = 0
                                        cur = Node(depth - 1, -playerNum, tempBoard,
                                                   Evaluate(tempBoard, eboard, playerNum))
                                        self.children.append(cur)

        print("ALL CHILDREN BOARDS")
        print(len(self.children))
        for i in range(len(self.children)):
            print(self.children[i].board)

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


def MiniMax(node, depth, playerNum, a, b):
    print("value")
    print(abs(node.value))
    if (depth == 0) or (abs(node.value) == maxsize):
        return node.value * playerNum
    if (playerNum > 0):
        bestValue = node.value * playerNum
        for i in range(len(node.children)):
            child = node.children[i]
            print("kid board")
            print(child.board)
            val = MiniMax(child, depth - 1, -playerNum, a, b)
            x = abs(maxsize * playerNum - val)
            y = abs(maxsize * playerNum - bestValue)
            print("past1")
            if (x < y):
                bestValue = val
            a = max(a, bestValue)
            if (a >= b):
                break
    else:
        bestValue = node.value * playerNum
        for i in range(len(node.children)):
            child = node.children[i]
            val = MiniMax(child, depth - 1, -playerNum, a, b)
            x = abs(maxsize * playerNum - val)
            y = abs(maxsize * playerNum - bestValue)
            print("past")
            if (x < y):
                bestValue = val
            b = min(b, bestValue)
            if (b <= a):
                break
    return bestValue


def GetNextMove(board, depth, playerNum):
    cur = Node(depth, playerNum, board, 0)

    # val = MiniMax(cur, depth, playerNum, 0, 0)

    # print(val)
    return cur.board

