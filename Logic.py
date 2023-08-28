import time
import pygame as p
import anim_essentials
import sys
from threading import stack_size
start=0
stop=0
def place_queens_dynamically(row,column,surface,n):
    anim_essentials.place_queen(row,column,surface,n)
    p.display.flip()
def is_safe(binary_board,row,column):
    n=len(binary_board)
    # checking for columns
    for i in range(column):
        if(binary_board[row][i]==1):
            return False
    # checking for queens in the same row
    for i in range(row):
        if(binary_board[i][column]==1):
            return False
    # checking for upper left diagonal from the current position
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)): # zip returns a tuple of both iterables combined
        if(binary_board[i][j]==1):
            return False
    for i,j in zip(range(row,n),range(column,-1,-1)):
        if(binary_board[i][j]==1):
            return False
    # checking for upper right diagonal
    return True
# The secondary diagonal is the right diagonal and the primary diagonal is the left diagonal

def solve_n_queens(column,binary_board,window,n):
     # initializing the board with all empty spaces initially
    if(column>=len(binary_board)):
        return True
    for i in range(len(binary_board)): # this is to iterate through all the columns to place the queens row by row
        if(is_safe(binary_board,i,column)):
            binary_board[i][column]=1
            place_queens_dynamically(i,column,window,n)
            time.sleep(2)
            if(solve_n_queens(column+1,binary_board,window,n)):
                return True
            binary_board[i][column]=0
            anim_essentials.erase_queen(i,column,window,n)
            time.sleep(2)
    return False
def visualizer(window,n):
    global start, stop
    binary_board=[[0]*n for i in range(n)]
    #print(binary_board)
    start=time.process_time()
    try:
        solve_n_queens(0,binary_board,window,n)
    except Exception as e:
        print(e)
    stop=time.process_time()
def main(window,n):
    visualizer(window,n)
if(__name__=="__main__"):

    # binary_board = [[1, 1, 1, 1],
    #                 [0, 1, 0, 0],
    #                 [0, 0, 0, 1],
    #                 [0, 0, 0, 0]]
    # start = time.process_time()  # Measures CPU time and not Wall time
    # res = is_safe(binary_board, 3, 2)
    # stop = time.process_time()
    # print(binary_board[0][2])
    # for i, row_list in enumerate(binary_board):
    #     for j in range(len(row_list)):
    #         if (binary_board[i][j] == 1):
    #             print(i, j)
    stack_size(4096 * 16)
    size = stack_size()
    print(size)