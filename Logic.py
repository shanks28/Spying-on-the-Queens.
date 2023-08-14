import Tester as test
import random
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
def main(window):
    # place_queens_dynamically(1,2,window)
    # place_queens_dynamically(2,2,window)
    for i in range(4):
        for j in range(4):
            if(i==j):
                place_queens_dynamically(i,j,window)