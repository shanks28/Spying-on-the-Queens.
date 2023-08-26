import time
import pygame as p
import anim_essentials
import cProfile
from line_profiler import LineProfiler
from memory_profiler import profile
start=0
stop=0
def place_queens_dynamically(row,column,surface,n):
    anim_essentials.place_queen(row,column,surface,n)
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

def solve_n_queens(row,binary_board,n):
     # initializing the board with all empty spaces initially
    if(row>=len(binary_board)):
        return True
    for i in range(len(binary_board)): # this is to iterate through all the columns to place the queens column by column
        if(is_safe(binary_board,row,i)):
            binary_board[row][i]=1
            # place_queens_dynamically(i,row,window,n)
            # time.sleep(.1)
            solve_n_queens(row+1,binary_board,n)
            binary_board[row][i]=0
            # anim_essentials.erase_queen(i,row,window,n)
            # time.sleep(.1)
    return False
def visualizer(n):
    binary_board=[[0]*n for i in range(n)]
    solve_n_queens(0,binary_board,n)
    print(binary_board)
def main(n):
    visualizer(n)
if(__name__=="__main__"):
    visualizer(9)
    # dict1 = {'(':0,')':0}
    # for i in user_input:
    #     if (i == '('):
    #         dict1['(']+=1
    #     else:
    #         dict1[')']+=1
    # if (dict1['('] == dict1[')']):
    #     print("balanced")
    # else:
    #     if (dict1['('] > dict1[')']):
    #         print("{} {} are required".format(dict1['('] - dict1[')'], ')'))
    #     else:
    #         print("{} {} are required".format(dict1[')'] - dict1['('], '('))
    # profiler=cProfile.Profile()
    # profiler.enable()
    # main(20)
    # profiler.disable()
    # profiler.print_stats(sort="cumulative")
    # def swap_brute_function(user_input):
    #     length=len(user_input)
    #     res_list=[]
    #
    #     for i in range(0,length-2,2):
    #         res_list.append(user_input[i+1])
    #         res_list.append(user_input[i])
    #     if(length%2==0):
    #         res_list.append(user_input[-1])
    #         res_list.append(user_input[-2])
    #     else:
    #         res_list.append(user_input[-1])
    #     return res_list
    # def merge(left,right):
    #     i,j,k=0,0,0
    #     m=len(left)
    #     n=len(right)
    #     res=[]
    #     while(i<m and j<n):
    #         res.append(left[i+1])
    #         j+=2
    #         res.append(right[j])
    #         i+=2
    #     while i<m:
    #         res.append(left[i])
    #         i+=1
    #     while j<n:
    #         res.append(right[j])
    #         j+=1
    #     return res
    # def swap_function_divide(user_input):
    #     if(len(user_input)<=1):
    #         return
    #     mid=len(user_input)//2
    #     left=user_input[:mid]
    #     right=user_input[mid:]
    #     swapped_left=swap_function_divide(left)
    #     swapper_right=swap_function_divide(right)
    #     res=merge(swapped_left,swapper_right)
    #     return  res
    # user_input=[12,42,9,30,56,20]
    # res=swap_function_divide(user_input)
    # print(res)
    pass