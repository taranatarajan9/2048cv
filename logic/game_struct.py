from directions import Direction
import random
import numpy as np

class GameBoard:
    def __init__(self):
        self.length = 4
        self.max = 2048
        self.board = []
        for row in range(self.length):
            self.board.append([])
            for _ in range(self.length):
                self.board[row].append(0)
        
        self.add_num()
        self.add_num()
        # self.board = [[0,2,2,0],[0,2,0,0],[0,2,0,0],[0,0,0,0]]
        
    
    def display(self):
        for row in self.board:
            print (row)

    def compress_board(self):
        new = []
        for j in range(self.length):
            partial_new = []
            for i in range(self.length):
                partial_new.append(0)
            new.append(partial_new)
        done = False
        for i in range(self.length):
            count = 0
            for j in range(self.length):
                if self.board[i][j] != 0:
                    new[i][count] = self.board[i][j]
                    if j != count:
                        done = True
                    count += 1
        return new, done

    def game_over(self): #return -1 for game not over, 0 for user loses, 1 for user wins
        for row in range(self.length):
            for col in range(self.length):
                if self.board[row][col] == 0:
                    return -1
                if self.board[row][col] == 2048:
                    return 1

        for i in range(self.length-1):
            for j in range(self.length-1):
                if self.board[i][j] == self.board[i+1][j] or self.board[i][j+1] == self.board[i][j]:
                    return -1
        for k in range(self.length-1):  # to check the left/right entries on the last row
            if self.board[self.length-1][k] == self.board[self.length-1][k+1]:
                return -1
        for j in range(self.length-1):  # check up/down entries on last column
            if self.board[j][self.length-1] == self.board[j+1][self.length-1]:
                return -1
        return 0

    def add_num(self): # Add a random 2 or 4 to the board
        add_two = random.randint(0,100) % 5 != 2

        x_coord = random.randint(0,100) % self.length
        y_coord = random.randint(0,100) % self.length

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
    
    # def clear_zeroes(self, dir): 
    #     if dir == Direction.up or dir == Direction.right:
    #         for row in range(self.length):
    #             for col in range(self.length):
    #                 if self.board[row][col] == 0:
    #                     if col == 3:
    #                         print('last col')
    #                     self.move_curr(dir, row, col)
    #     else:
    #         for row in reversed(range(self.length)):
    #             for col in reversed(range(self.length)):
    #                 if self.board[row][col] == 0:
    #                     self.move_curr(dir, row, col)
    
    # def get_positions(self, dir, row, col):
    #     points = []
    #     if 