from sys import maxsize

class Node(object):
    def __init__(self, depth, playerNum, board, value = 0):
        self.depth = depth
        self.playerNum = playerNum
        self.value = value
        self.children = []
        self.board = GetBoardEvals(depth)
        self.CreateChildren(board)


    def CreateChildren(board):
        if self.depth >= 0:
            for i in range(1, 3):
                v = self.i_sticksRemaining = i
                self.children.append( Node( self.depth - 1, -self.playerNum, v, self.RealVal(v)))

    def RealVal(selfself, value):
        if(value == 0):
            return maxsize * self.playerNum
        elif(value < 0):
            return maxsize * -self.playerNum
        return 0

    # generates a general board evaluation based on the dimensions of the board
    def GetBoardEvals(d):
        board = []
        for i in d-1:
            for j in d-1:
                board[i][j] = i
        return board


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
        else:
            bestValue = maxsize * playerNum
            for i in range(len(node.children)):
                child = node.children[i]
                val = MiniMax(child, depth - 1, -playerNum, a ,b)
                if (abs(maxsize * playerNum - val) < abs(maxsize * playerNum - bestValue)):
                    bestValue = val
                b = min(b, bestValue)
                if(b <= a):
                    break

        return bestValue
