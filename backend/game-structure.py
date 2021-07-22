import directions 
import random

class GameBoard:
    def __init__(self):
        self.length = 4
        self.max = 2048
        self.board = []
        for row in range(self.length):
            self.board.append([])
            for _ in range(self.length):
                self.board[row].append(0)
        
    def move(self, direction): # function to modify board however the player wants to move
        if direction == directions.Direction.up:
            
                    # update the board to move the lower spaces up one space 

    def move_curr(self, direction, current_y, current_x): # helper function for when two blocks are added
        if direction == directions.Direction.up:
            for y_coord in range(current_y + 1, self.length-1):
                self.board[y_coord][current_x] = self.board[y_coord+1][current_x]
            self.board[self.length-1][current_x] = 0

        if direction == directions.Direction.down:
            for y_coord in reversed(range(1, current_y - 1)):
                self.board[y_coord][current_x] = self.board[y_coord-1][current_x]
            self.board[1][current_x] = 0
        
        if direction == directions.Direction.right:
            for x_coord in range(current_x + 1, self.length - 1):
                self.board[current_y][x_coord] = self.board[current_y][x_coord + 1]
            self.board[current_y][self.length - 1] = 0
        
        if direction == directions.Direction.left:
            for x_coord in reversed(range(1, current_x - 1)):
                self.board[current_y][x_coord] = self.board[current_y][x_coord - 1]
            self.board[current_y][1] = 0
    
    def combine(self, direction, current_x, current_y): # helper function to check if there are two tiles to be combined
        if direction == directions.Direction.up and current_y < self.length - 1:
            if (self.board[current_y][current_x] == self.board[current_y + 1][current_x]):
                self.board[current_y][current_x] *= 2
        
        if direction == directions.Direction.down and current_y > 0:
            if self.board[current_y][current_x] == self.board[current_y - 1][current_x]:
                self.board[current_y][current_x] *= 2
        
        if direction == directions.Direction.left and current_x > 0:
            if (self.board[current_x] == self.board[current_x - 1]):
                self.board[current_y][current_x] *= 2
        
        if direction == directions.Direction.right and current_x < self.length - 1:
            if self.board[current_y][current_x] == self.board[current_y][current_x + 1]:
                 self.board[current_y][current_x] *= 2

    def game_over(self): # check if there are no matches 
        for row in range(1, self.length - 1):
            for col in range(1, self.length - 1):
                if col > 0:
                    if self.board[row][col] == self.board[row][col-1]:
                        return False
                if row > 0:
                    if self.board[row][col] == self.board[row-1][col]:
                        return False
                if row < self.length - 1:
                    if self.board[row][col] == self.board[row+1][col]:
                        return False
                if col < self.length - 1:
                    if self.board[row][col] == self.board[row][col+1]:
                        return False

        return True

    def add_num(self): # Add a random 2 or 4 to the board
        add_two = random.randint() % 5 != 2

        x_coord = random.randint() % self.length
        y_coord = random.randint() % self.length

        count = 0 
        while (self.board[x_coord][y_coord] != 0):
            count += 1
            if (count == self.length * self.length):
                return [-1,-1]
            if x_coord == self.length - 1:
                x_coord = -1
            if y_coord == self.length - 1:
                y_coord = -1
            x_coord += 1
            y_coord += 1
        
        if (add_two):
            self.board[x_coord][y_coord] = 2
        else:
            self.board[x_coord][y_coord] = 4
        
        return [x_coord, y_coord]
    
    def clear_zeroes(self, dir): 
        for row in range(self.length):
            for col in range(self.length):
                if self.board[row][col] == 0:
                    move_curr(self, dir, row, col)
