import random
import time

import anim_essentials

def convert_binary_board(board):
    n = len(board)

    # Initialize an empty binary board with all 0s
    binary_board=[[0]*n for i in range(n)]

    # Place queens on the board by setting the corresponding elements to 1
    for col, row in enumerate(board):
        binary_board[row][col] = 1
    return binary_board
def h_cost(board):
    conflicts=0
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if board[i]==board[j]: # checking the row conflicts
                conflicts+=1
            slope=j-i
            if(board[i]==board[j]-slope or board[i]==board[j]+slope): # y=mx+c
                conflicts+=1
    return conflicts
def visualizer(window,n):
    board = []
    for num in range(n):
        randint = random.randint(0, n - 1)
        board.append(randint)# the Indices represent the cols and values represent the rows
    print(board)
    print(h_cost(board))
    board = convert_binary_board(board)
    for row,rowlist in enumerate(board):
        for col, val in enumerate(rowlist):
            if val == 1:
                anim_essentials.place_queen(row,col,window,n)
                time.sleep(.1)

if(__name__=="__main__"):
    board=[]
    n=int(input("Enter the number of queens you want to place: "))
    for num in range(n):
        randint=random.randint(0,n-1)
        board.append(randint)
    print(board)
    board=convert_binary_board(board)
    for row in board:
        for col,val in enumerate(row):
            if val==1:
                pass

