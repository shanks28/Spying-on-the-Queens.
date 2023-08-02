import pygame as p
def number_of_queens_8():
    return 8
def number_of_queens_4():
    return 4
window_dimensions=[400,400]
p.init() # when we call this function we essentially call the lower level p.display.init() function
flags=p.RESIZABLE|p.HWSURFACE|p.DOUBLEBUF
window=p.display.set_mode((window_dimensions[0],window_dimensions[1]),flags)
rows=[1,2,3,4,5,6,7,8]
columns=['A','B','C','D','E','F','G','H']
pos_x,pos_y=(0,0)
black=(0,0,0)
white=(255,255,255)
running=True
while(running):
    for event in p.event.get():
        if(event.type==p.QUIT):
            running=False

    window.fill(white)
p.display.quit() # this is already handled when the program exits and is harmless to call it again