import random
def convert_binary_board(board):
    # Determine the size of the board (N x N)
    n = len(board)

    # Initialize an empty binary board with all 0s
    binary_board=[[0]*n for i in range(n)]

    # Place queens on the board by setting the corresponding elements to 1
    for col, row in enumerate(board):
        binary_board[row][col] = 1
    binary_board.reverse()
    return binary_board
if(__name__=="__main__"):
    board=[]
    n=int(input("Enter the number of queens you want to place: "))
    for num in range(n):
        randint=random.randint(0,n-1)
        board.append(randint)
    print(board)
    board=convert_binary_board(board)
    print(board)