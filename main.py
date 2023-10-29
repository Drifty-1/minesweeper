from game import Game
from board import Board
size = (3, 3) #change this to adjust number of tiles on grid (difficulty level)
prob = 0.1 #change this to adjust probability (number) of bombs
board = Board(size, prob)
screenSize = (800, 800) #change this in accordance with size to make tiles square-shaped
game = Game(board, screenSize)
game.run() #run

