import Tester as test
import random
import time
import pygame as p
import anim_essentials
start=0
stop=0
def place_queens_dynamically(row,column,surface):
    test.place_queen(row,column,surface)
    p.display.flip()
def is_safe(binary_board,row,column):
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


def solve_n_queens(column,binary_board,window):
     # initializing the board with all empty spaces initially
    if(column>=len(binary_board)):
        return True
    for i in range(len(binary_board)): # this is to iterate through all the columns to place the queens column by column
        if(is_safe(binary_board,column,i)):
            binary_board[column][i]=1
            place_queens_dynamically(column,i,window)
            time.sleep(1)
            if(solve_n_queens(column+1,binary_board,window)):
                return True
            binary_board[column][i]=0
            anim_essentials.erase_queen(column,i,window)
            time.sleep(1)
    return False
def visualizer(window,n):
    global start, stop
    binary_board=[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
    start=time.process_time()
    solve_n_queens(0,binary_board,window)
    stop=time.process_time()
    # start = time.process_time()  # Measures CPU time and not Wall time
    # for i, row_list in enumerate(binary_board):
    #     for j in range(len(row_list)):
    #         if (binary_board[i][j] == 1):
    #             place_queens_dynamically(j, i, window)
    #             time.sleep(1)
    #             # place_queens_dynamically(0,2,window)
    # anim_essentials.erase_queen(1, 0, window)
    # time.sleep(1)
    # stop = time.process_time()
    # print(stop - start)
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
    binary_board=[[0]*4]*4

    print(binary_board)