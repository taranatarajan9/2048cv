from game_struct import GameBoard
from directions import Direction
board = GameBoard()
board.display()
board.move(Direction.up) # these dont work
print(" ")
board.display()
# board.move(Direction.right) 
# print(" ")
# board.display()