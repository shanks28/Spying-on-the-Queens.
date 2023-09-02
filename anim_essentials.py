import pygame as p
import GUI
def erase_queen(row,column,window,n):
    square_size=(window.get_width()//n)-5 # this is for the size of the square
    pos_x=row*square_size
    pos_y=column*square_size
    if not (row+column)%2:
        color=(255,255,255)
    else:
        color=(0,0,0)
    p.draw.rect(window,color,(pos_y,pos_x,square_size,square_size))
    p.display.flip()
def place_queen(row,column,window,n):
    image=p.image.load("white_queen_chess_piece_by_prussiaart_dcpq5fx-pre.png")
    square_size = (window.get_width()/ n) - 5
    image=p.transform.scale(image,(square_size-5,square_size-5)) # this takes image object,width,length of the object
    x=row*square_size
    y=column*square_size
    window.blit(image,(y,x)) # this method is acted on the surface object and takes the image to put on the surface followed by the position of the image
    p.display.flip()