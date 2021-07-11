import directions 


class GameBoard:
    def __init__(self):
        self.length = 4
        self.max = 2048
        self.board = []
        for row in range(self.length):
            self.board.append([])
            for _ in range(self.length):
                self.board[row].append(0)
        
    def move(self, Direction): # function to modify board however the player wants to move
        for row in range(1,self.length):
            for col in range(self.length):
                
                if self.board[row-1][col] == self.board[row-1][col]:
                    self.board[row-1][col] *= 2
                    # update the board to move the lower spaces up one space 

    def move_up(self, Direction, current_x, current_y): # helper function for when two blocks are added
        if 
        