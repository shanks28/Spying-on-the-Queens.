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
    n=len(binary_board)# number of rows ...or the number queens to be placed
    for i in range(column):
        if(binary_board[row][i]==1):
            return False
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)):# this is for the upper left diagonal we could also do upper right(Upper left is also called as the normal diagonal)
        # The right diagonal or antidiagonal is another method to implement this
        if(binary_board[i][j]==1):
            return False
    for i,j in zip(range(row,n,1),range(column,-1,-1)): # this is for the lower left diagonal
        if(binary_board[i][j]==1):
            return False
    return True


def solve_4_queens():
    pass

def main(window):
    place_queens_dynamically(1,2,window)
    place_queens_dynamically(2,2,window)
if(__name__=="__main__"):
    binary_board=[[0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,0],
                  [0,0,0,0]]
    res=is_safe(binary_board,2,1)
    print(res)
