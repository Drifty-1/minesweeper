class Piece(): #each tile on the board
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False #at the start nothing is clicked
        self.flagged = False #at the start nothing is flagged

    #returns piece modifications
    def getHasBomb(self):
        return self.hasBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self): # counts the bombs around a piece
        self.numAround = 0
        for piece in self.neighbors:
            if (piece.getHasBomb()):
                self.numAround += 1
        

    def getNumAround(self): #returns number of bombs around
        return self.numAround
    
    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True


    def getNeighbors(self): #returns list of neighbors
        return self.neighbors