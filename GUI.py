import pygame as p
import tkinter as tk
def draw_4_queens():
    for rows in range(0, 4):
        for columns in range(0, 4):
            pos_x = (rows * square_size)
            pos_y = (columns * square_size)

            if ((rows + columns) % 2):
                p.draw.rect(window, black, (pos_x, pos_y, square_size, square_size))
            else:
                p.draw.rect(window, white, (pos_x, pos_y, square_size, square_size))
if(__name__=="__main__"):

    window_dimensions=[800,800]
    p.init() # when we call this function we essentially call the lower level p.display.init() function
    flags=p.RESIZABLE|p.HWSURFACE|p.DOUBLEBUF
    window=p.display.set_mode((window_dimensions[0],window_dimensions[1]),flags)
    rows=[1,2,3,4,5,6,7,8]
    columns=['A','B','C','D','E','F','G','H']
    pos_x,pos_y=(0,0)
    black=(0,0,0)
    white=(255,255,255)
    square_size=(window_dimensions[0]/4)
    clock=p.time.Clock()
    running=True
    while(running):
        for event in p.event.get():
            if(event.type==p.QUIT):
                running=False
        draw_4_queens()
        p.display.flip()
        window.fill(white)
        clock.tick(60)
    p.display.quit() # this is already handled when the program exits and is harmless to call it again