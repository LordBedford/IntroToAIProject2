# Brian Tran
from sys import maxsize

class Node(object):
    def __init__(self, depth, playerNum, board, value = 0):
        self.depth = depth
        self.playerNum = playerNum # negative playerNum = AI agent
        self.value = value
        self.children = []
        self.board = board
        self.CreateChildren(self.depth, self.board, self.playerNum)


    def CreateChildren(self, depth, board, playerNum):
        if self.depth >= 0:
            eboard = GetBoardEvals(depth, board)
            tempBoard = board
            validChildren = []
            for i in range (depth):
                for j in range (depth):
                    # AI agent's turn (4->2, 6->1, 5->3)
                    if(playerNum < 0):
                        if(board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6):
                            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i + 1, j - 1),
                                         (i - 1, j + 1),
                                         (i - 1, j - 1)]
                            for next in neighbors:
                                # Checks to see if neighbors are within Bounds
                                if next[0] < 0 or \
                                        next[1] < 0 or \
                                        next[0] >= depth or \
                                        next[1] >= depth:
                                    continue
                                validChildren.append(next)
                            if(board[i][j] == 4):
                                # Checks to see if neighbors can kill units
                                for next in validChildren:
                                    # Heros can't kill mage
                                    if board[next[0]][next[1]] == 3:
                                        continue
                                    # Hero kills wumpus
                                    if board[next[0]][next[1]] == 2:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 4
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                    # Heros Tie and kill each other
                                    if board[next[0]][next[1]] == 1:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    print("here")
                                    tempBoard[next[0]][next[1]] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


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
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                    # Wumpus Tie and kill each other
                                    if board[next[0]][next[1]] == 2:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[next[0]][next[1]] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


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
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                    # Mages Tie and kill each other
                                    if board[next[0]][next[1]] == 3:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[next[0]][next[1]] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                    # Player's turn
                    elif(playerNum > 0):
                        if(board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3):
                            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i + 1, j - 1),
                                         (i - 1, j + 1),
                                         (i - 1, j - 1)]
                            for next in neighbors:
                                # Checks to see if neighbors are within Bounds
                                if next[0] < 0 or \
                                        next[1] < 0 or \
                                        next[0] >= depth or \
                                        next[1] >= depth:
                                    continue
                                validChildren.append(next)
                            if(board[i][j] == 1):
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
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                    # Heros Tie and kill each other
                                    if board[next[0]][next[1]] == 4:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[next[0]][next[1]] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

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
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                    # Wumpus Tie and kill each other
                                    if board[next[0]][next[1]] == 5:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[next[0]][next[1]] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

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
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                    # Mages Tie and kill each other
                                    if board[next[0]][next[1]] == 6:
                                        tempBoard = board
                                        tempBoard[next[0]][next[1]] = 0
                                        tempBoard[i][j] = 0
                                        self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                                  self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[next[0]][next[1]] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

# calculates current value of board based on number of pieces and center board positioning
def Evaluate(board, eboard, playerNum):
    aiCount = 0
    playerCount = 0
    aiBoardValue = 0
    playerBoardValue = 0
    value = 0
    for i in len(board) - 1:
        for j in len(board) - 1:
            if (board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3):
                aiCount = aiCount + 10
                aiBoardValue = eboard[i][j]
                aiCount = aiCount + aiBoardValue
            elif(board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6):
                playerCount = playerCount + 10
                playerBoardValue = eboard[i][j]
                playerCount = aiCount + playerBoardValue
    return playerCount - aiCount


# generates a general board evaluation based on the dimensions of the board
def GetBoardEvals(d, board):
    eboard = []
    center = d//2
    # assign higher values for centralized cells
    for i in d-1:
        for j in d-1:
            eboard[i][j] = 0
    if d == 3:
        eboard[center][center] = 3
    if d == 6:
        eboard[center][center] = 2
        eboard[center +1][center] = 2
        eboard[center + 1][center + 1] = 2
        eboard[center][center +1] = 2
    if d == 9:
        eboard[center][center] = 2
        eboard[center + 1][center] = 2
        eboard[center + 1][center + 1] = 2
        eboard[center][center + 1] = 2
        eboard[center + 2][center] = 2
        eboard[center + 2][center + 1] = 2
        eboard[center + 2][center + 2] = 2
        eboard[center][center + 2] = 2
        eboard[center + 1][center+ 2] = 2

    # if pit, assign value of -10
    for i in d - 1:
        for j in d - 1:
            if board[i][j] == 7:
                eboard[i][j] = -10
    return eboard


def MiniMax(node, depth, playerNum, a, b):
     if(depth == 0) or (abs(node.value) == maxsize):
        return node.value
     if(playerNum > 0):
        bestValue = maxsize * playerNum
        for i in range(len(node.children)):
            child = node.children[i]
            val = MiniMax(child, depth - 1, -playerNum, a, b)
            if(abs(maxsize * playerNum - val) < abs(maxsize * playerNum - bestValue)):
                bestValue = val
            a = max(a, bestValue)
            if(a >= b):
                break
            return bestValue
     else:
        bestValue = maxsize * playerNum
        for i in range(len(node.children)):
            child = node.children[i]
            val = MiniMax(child, depth - 1, -playerNum, a, b)
            if (abs(maxsize * playerNum - val) < abs(maxsize * playerNum - bestValue)):
                bestValue = val
            b = min(b, bestValue)
            if (b <= a):
                break
            return bestValue


def GetNextMove(board, depth, playerNum):
    cur = Node(depth, playerNum, board, 0)
    val = MiniMax(cur, depth, playerNum, None, None)
    return cur.board