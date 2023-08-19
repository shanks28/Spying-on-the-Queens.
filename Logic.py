import Tester as test
import random
import time
import pygame as p
# we consider the board in this module as a 2D array of rows and column
'''
    we know that there can be only 1 queen per row
    Consider the board as a matrix

    '''
# draw_object=draw_pygame_window()
# row_length,col_lemgth=(4,4)
# for row in range(row_length):
#     for col in range(col_lemgth):
#         pass
def place_queens_dynamically(row,column,surface):
    test.place_queen(row,column,surface)
def is_safe(binary_board,row,column): # this implementation places only 1 queen per row and hence does not check for the presence of queen in another row
    n=len(binary_board)
    # checking for columns
    for i in range(n):
        if(binary_board[row][i]==1):
            return False
    # checking for queens in the same row
    for i in range(n):
        if(binary_board[i][column]==1):
            return False
    # checking for upper left diagonal from the current position
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)): # zip returns a tuple of both iterables combined
        if(binary_board[i][j]==1):
            return False
    for i,j in zip(range(row,-1,-1),range(column,n)):
        if(binary_board[i][j]==1):
            return False
    # checking for upper right diagonal
    return True


def solve_4_queens():
    pass

def main(window):
    binary_board = [[0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 0, 0]]
    start = time.process_time()  # Measures CPU time and not Wall time
    res = is_safe(binary_board, 3, 2)
    stop = time.process_time()
    for i,row_list in enumerate(binary_board):
        for j in range(len(row_list)):
            if (binary_board[i][j] == 1):
                place_queens_dynamically(j,i,window)
                #place_queens_dynamically(0,2,window)
if(__name__=="__main__"):

    binary_board = [[0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 0, 0]]
    start = time.process_time()  # Measures CPU time and not Wall time
    res = is_safe(binary_board, 3, 2)
    stop = time.process_time()
    print(binary_board[0][2])
    for i, row_list in enumerate(binary_board):
        for j in range(len(row_list)):
            if (binary_board[i][j] == 1):
                print(i, j)
