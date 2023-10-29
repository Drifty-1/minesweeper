from piece import Piece
from random import random
from time import sleep
# setting up board

class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob #probability that each piece has a bomb
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.setBoard()

    def setBoard(self): #setting board function
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                piece = Piece(hasBomb)
                row.append(piece) #adding pieces to row list
            self.board.append(row) #adding row list onto board
        self.setNeighbors()

    def setNeighbors(self): #adjacent bombs
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getListOfNeighbors(self, index): #returns list of adjacent squares
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1] #check for adjacent squares out of bounds
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors

    def getSize(self): #returns size of object for piece size
        return self.size
    
    def getPiece(self, index): #returns piece location
        return self.board[index[0]][index[1]]
    
    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())): #cant click on a flagged piece or already clicked piece
            return 
        if (flag): #toggles whether piece is flagged or not
            piece.toggleFlag()
            return
        piece.click()
        if (piece.getHasBomb()): #loses if click bomb
            self.lost = True
            return
        self.numClicked += 1 #increases number of clicked pieces
        if (piece.getNumAround() != 0):
            return
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getClicked()): #recursive click does not click a bomb
                self.handleClick(neighbor, False) #recursive clicks on adjacent squares, False for not flagging it

    
    '''win/loss conditions'''
    def getLost(self):
        return self.lost
    def getWon(self):
        return self.numNonBombs == self.numClicked