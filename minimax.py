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
            for i in depth - 1:
                for j in depth - 1:
                    # AI agent's turn (4->2, 6->1, 5->3)
                    if(playerNum < 0):
                        if(board[i][j] == 4):
                            # 1/8 Right limit good and not hero vs mage
                            if(i+1 < depth and board[i+1][j] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j] == 1):
                                    tempBoard[i+1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j] == 2):
                                    tempBoard[i + 1][j] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 2/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j-1 > 0 and board[i+1][j-1] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j-1] == 1):
                                    tempBoard[i+1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j-1] == 2):
                                    tempBoard[i + 1][j-1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j-1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 3/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j+1 < depth and board[i+1][j+1] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j+1] == 1):
                                    tempBoard[i+1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j+1] == 2):
                                    tempBoard[i + 1][j+1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j+1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 4/8 Right limit good and not hero vs mage
                            if(j+1 < depth and board[i][j+1] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j+1] == 1):
                                    tempBoard[i][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j+1] == 2):
                                    tempBoard[i][j+1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j+1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 5/8 Right limit good and not hero vs mage
                            if(j-1 > 0 and board[i][j-1] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j-1] == 1):
                                    tempBoard[i][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j-1] == 2):
                                    tempBoard[i][j-1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j-1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 6/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j+1 < depth and board[i-1][j+1] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j+1] == 1):
                                    tempBoard[i-1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j+1] == 2):
                                    tempBoard[i-1][j+1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j+1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 7/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j-1 > 0 and board[i-1][j-1] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j-1] == 1):
                                    tempBoard[i-1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j-1] == 2):
                                    tempBoard[i-1][j-1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j-1] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 8/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and board[i-1][j] != 3):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j] == 1):
                                    tempBoard[i-1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j] == 2):
                                    tempBoard[i-1][j] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i -1][j] = 4
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                        # Wizard
                        elif(board[i][j] == 6):
                            # 1/8 Right limit good and not wizard vs wumpus
                            if(i+1 < depth and board[i+1][j] != 2):
                                tempBoard = board
                                # mage vs mage, both spots set to grass
                                if(board[i+1][j] == 3):
                                    tempBoard[i+1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # mage vs hero, mage wins
                                elif(board[i+1][j] == 1):
                                    tempBoard[i + 1][j] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 2/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j-1 > 0 and board[i+1][j-1] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j-1] == 3):
                                    tempBoard[i+1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j-1] == 1):
                                    tempBoard[i + 1][j-1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j-1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 3/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j+1 < depth and board[i+1][j+1] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j+1] == 3):
                                    tempBoard[i+1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j+1] == 1):
                                    tempBoard[i + 1][j+1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j+1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 4/8 Right limit good and not hero vs mage
                            if(j+1 < depth and board[i][j+1] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j+1] == 3):
                                    tempBoard[i][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j+1] == 1):
                                    tempBoard[i][j+1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j+1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 5/8 Right limit good and not hero vs mage
                            if(j-1 > 0 and board[i][j-1] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j-1] == 3):
                                    tempBoard[i][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j-1] == 1):
                                    tempBoard[i][j-1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j-1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 6/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j+1 < depth and board[i-1][j+1] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j+1] == 3):
                                    tempBoard[i-1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j+1] == 1):
                                    tempBoard[i-1][j+1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j+1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 7/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j-1 > 0 and board[i-1][j-1] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j-1] == 3):
                                    tempBoard[i-1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j-1] == 1):
                                    tempBoard[i-1][j-1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j-1] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 8/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and board[i-1][j] != 2):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j] == 3):
                                    tempBoard[i-1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j] == 1):
                                    tempBoard[i-1][j] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i -1][j] = 6
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))



                        # Wumpus
                        elif(board[i][j] == 5):
                            # 1/8 Right limit good and not hero vs mage
                            if(i+1 < depth and board[i+1][j] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j] == 2):
                                    tempBoard[i+1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j] == 3):
                                    tempBoard[i + 1][j] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 2/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j-1 > 0 and board[i+1][j-1] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j-1] == 2):
                                    tempBoard[i+1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j-1] == 3):
                                    tempBoard[i + 1][j-1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j-1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 3/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j+1 < depth and board[i+1][j+1] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j+1] == 2):
                                    tempBoard[i+1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j+1] == 3):
                                    tempBoard[i + 1][j+1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j+1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 4/8 Right limit good and not hero vs mage
                            if(j+1 < depth and board[i][j+1] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j+1] == 2):
                                    tempBoard[i][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j+1] == 3):
                                    tempBoard[i][j+1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j+1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 5/8 Right limit good and not hero vs mage
                            if(j-1 > 0 and board[i][j-1] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j-1] == 2):
                                    tempBoard[i][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j-1] == 3):
                                    tempBoard[i][j-1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j-1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 6/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j+1 < depth and board[i-1][j+1] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j+1] == 2):
                                    tempBoard[i-1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j+1] == 3):
                                    tempBoard[i-1][j+1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j+1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 7/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j-1 > 0 and board[i-1][j-1] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j-1] == 2):
                                    tempBoard[i-1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j-1] == 3):
                                    tempBoard[i-1][j-1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j-1] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 8/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and board[i-1][j] != 1):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j] == 2):
                                    tempBoard[i-1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j] == 3):
                                    tempBoard[i-1][j] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i -1][j] = 5
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))



                    # Player's turn (1->5, 3->4, 2->6)
                    elif(playerNum > 0):
                        if(board[i][j] == 1):
                            # 1/8 Right limit good and not hero vs mage
                            if(i+1 < depth and board[i+1][j] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j] == 4):
                                    tempBoard[i+1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j] == 5):
                                    tempBoard[i + 1][j] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 2/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j-1 > 0 and board[i+1][j-1] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j-1] == 4):
                                    tempBoard[i+1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j-1] == 5):
                                    tempBoard[i + 1][j-1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j-1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 3/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j+1 < depth and board[i+1][j+1] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j+1] == 4):
                                    tempBoard[i+1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j+1] == 5):
                                    tempBoard[i + 1][j+1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j+1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 4/8 Right limit good and not hero vs mage
                            if(j+1 < depth and board[i][j+1] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j+1] == 4):
                                    tempBoard[i][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j+1] == 5):
                                    tempBoard[i][j+1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j+1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 5/8 Right limit good and not hero vs mage
                            if(j-1 > 0 and board[i][j-1] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j-1] == 4):
                                    tempBoard[i][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j-1] == 5):
                                    tempBoard[i][j-1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j-1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 6/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j+1 < depth and board[i-1][j+1] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j+1] == 4):
                                    tempBoard[i-1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j+1] == 5):
                                    tempBoard[i-1][j+1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j+1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 7/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j-1 > 0 and board[i-1][j-1] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j-1] == 4):
                                    tempBoard[i-1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j-1] == 5):
                                    tempBoard[i-1][j-1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j-1] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 8/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and board[i-1][j] != 6):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j] == 4):
                                    tempBoard[i-1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j] == 5):
                                    tempBoard[i-1][j] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i -1][j] = 1
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                        # Wizard
                        elif(board[i][j] == 3):
                            # 1/8 Right limit good and not wizard vs wumpus
                            if(i+1 < depth and board[i+1][j] != 5):
                                tempBoard = board
                                # mage vs mage, both spots set to grass
                                if(board[i+1][j] == 6):
                                    tempBoard[i+1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # mage vs hero, mage wins
                                elif(board[i+1][j] == 4):
                                    tempBoard[i + 1][j] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 2/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j-1 > 0 and board[i+1][j-1] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j-1] == 6):
                                    tempBoard[i+1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j-1] == 4):
                                    tempBoard[i + 1][j-1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j-1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 3/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j+1 < depth and board[i+1][j+1] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j+1] == 6):
                                    tempBoard[i+1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j+1] == 4):
                                    tempBoard[i + 1][j+1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j+1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 4/8 Right limit good and not hero vs mage
                            if(j+1 < depth and board[i][j+1] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j+1] == 6):
                                    tempBoard[i][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j+1] == 4):
                                    tempBoard[i][j+1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j+1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 5/8 Right limit good and not hero vs mage
                            if(j-1 > 0 and board[i][j-1] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j-1] == 6):
                                    tempBoard[i][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j-1] == 4):
                                    tempBoard[i][j-1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j-1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 6/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j+1 < depth and board[i-1][j+1] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j+1] == 6):
                                    tempBoard[i-1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j+1] == 4):
                                    tempBoard[i-1][j+1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j+1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 7/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j-1 > 0 and board[i-1][j-1] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j-1] == 6):
                                    tempBoard[i-1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j-1] == 4):
                                    tempBoard[i-1][j-1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j-1] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 8/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and board[i-1][j] != 5):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j] == 6):
                                    tempBoard[i-1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j] == 4):
                                    tempBoard[i-1][j] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i -1][j] = 3
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))



                        # Wumpus
                        elif(board[i][j] == 2):
                            # 1/8 Right limit good and not hero vs mage
                            if(i+1 < depth and board[i+1][j] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j] == 5):
                                    tempBoard[i+1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j] == 6):
                                    tempBoard[i + 1][j] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 2/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j-1 > 0 and board[i+1][j-1] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j-1] == 5):
                                    tempBoard[i+1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j-1] == 6):
                                    tempBoard[i + 1][j-1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j-1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 3/8 Right limit good and not hero vs mage
                            if(i+1 < depth and j+1 < depth and board[i+1][j+1] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i+1][j+1] == 5):
                                    tempBoard[i+1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i+1][j+1] == 6):
                                    tempBoard[i + 1][j+1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i + 1][j+1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                            # 4/8 Right limit good and not hero vs mage
                            if(j+1 < depth and board[i][j+1] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j+1] == 5):
                                    tempBoard[i][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j+1] == 6):
                                    tempBoard[i][j+1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j+1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 5/8 Right limit good and not hero vs mage
                            if(j-1 > 0 and board[i][j-1] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i][j-1] == 5):
                                    tempBoard[i][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i][j-1] == 6):
                                    tempBoard[i][j-1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i][j-1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 6/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j+1 < depth and board[i-1][j+1] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j+1] == 5):
                                    tempBoard[i-1][j+1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j+1] == 6):
                                    tempBoard[i-1][j+1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j+1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 7/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and j-1 > 0 and board[i-1][j-1] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j-1] == 5):
                                    tempBoard[i-1][j-1] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j-1] == 6):
                                    tempBoard[i-1][j-1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i - 1][j-1] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))


                            # 8/8 Right limit good and not hero vs mage
                            if(i-1 > 0 and board[i-1][j] != 4):
                                tempBoard = board
                                # Hero vs hero, both spots set to grass
                                if(board[i-1][j] == 5):
                                    tempBoard[i-1][j] = 0
                                    tempBoard[i][j] = 0
                                    self.children.append( Node( self.depth - 1, -self.playerNum, tempBoard, self.Evaluate(board, eboard, playerNum)))

                                # Hero vs wumpus, hero wins
                                elif(board[i-1][j] == 6):
                                    tempBoard[i-1][j] = 2
                                    tempBoard[i][j] = 0
                                    self.children.append(Node(self.depth - 1, -self.playerNum, tempBoard,
                                                              self.Evaluate(board, eboard, playerNum)))

                                # Open Space
                                else:
                                    tempBoard[i -1][j] = 2
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
    for i in depth - 1:
        for j in depth - 1:
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