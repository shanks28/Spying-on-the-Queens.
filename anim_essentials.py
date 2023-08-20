import pygame
def erase_queen(row,column,window):
    square_size=window.get_width()//4-5 # this is for the size of the square
    pos_x=row*square_size
    pos_y=column*square_size
    if not (row+column)%2:
        color=(255,255,255)
    else:
        color=(0,0,0)
    pygame.draw.rect(window,color,(pos_x,pos_y,square_size,square_size))
    pygame.display.flip()
