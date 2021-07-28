from game_struct import GameBoard
from directions import Direction
directs = {'up': Direction.up, "down": Direction.down, "left": Direction.left, "right": Direction.right}
board = GameBoard()
board.display()

input_prompt = "Type a direction (Up, Down, Left, or Right) or Q to quit the game: "
input_str = input(input_prompt)
dir_str = input_str.split(" ")[0].lower()
while dir_str !=  "q" and not board.game_over():
    board.move(directs[dir_str])
    print(" ")
    board.display()
    input_str = input(input_prompt)
    dir_str = input_str.split(" ")[0].lower()
    
print("Game Over")