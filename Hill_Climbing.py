import random
import time
import anim_essentials
start,stop=(0,0)
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
def simple_hill_climbing(n,max_iterations):
    board=[]
    for num in range(n):
        randint = random.randint(0, n - 1) # generating a random configuration as a seed state

        board.append(randint)  # the Indices represent the cols and values represent the rows

    conflicts=h_cost(board)  # heuristic cost of the seed state
    for i in range(max_iterations):# giving it an ultimatum
        neighbor_config=list(board)
        queen_choice=random.randint(0,n-1)
        next_row=random.randint(0,n-1)
        neighbor_config[queen_choice]=next_row
        new_conflicts=h_cost(neighbor_config) # getting the heuristic cost of the new configuration

        if(new_conflicts< conflicts): # a better solution has been attained
            board=neighbor_config
            conflicts=new_conflicts
        if(conflicts==0): # global minima reached
            return board
    return board

def visualizer(window,n):
    global start,stop
    start=time.process_time()
    board=simple_hill_climbing(n,1000)
    stop=time.process_time()
    binary_board = convert_binary_board(board) # converting the random config board to a binary_board
    for row,rowlist in enumerate(binary_board):
        for col, val in enumerate(rowlist):
            if val == 1:
                anim_essentials.place_queen(row,col,window,n)
                time.sleep(.1)
    print(h_cost(board))
if(__name__=="__main__"):
    max_iterations=100

