import pygame
pygame.init()
window_dimensions=[800,800]
flags=pygame.RESIZABLE|pygame.HWSURFACE|pygame.DOUBLEBUF
window=pygame.display.set_mode((window_dimensions[0],window_dimensions[1]),flags)
clock=pygame.time.Clock()
running=True
chessboard_size_8_queens=4
square_size=window_dimensions[0]/chessboard_size_8_queens
white=(255,255,255)# this stores the color as an RGB tuple
black=(0,0,0)
def for_8_queens():
    for row in range(chessboard_size_8_queens):
        for col in range(chessboard_size_8_queens):
            y=row*square_size
            x=col*square_size
            if((row+col)%2==0):
                color=white
            else:
                color=black
            pygame.draw.rect(window,color,(x,y,square_size,square_size))
while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
    window.fill(white)
    # clock.tick(60) # this is to limit the number of frames that get displayed on the screen persec
    for_8_queens()
    pygame.display.flip()
pygame.quit()
def absolute_difference(list1,list2):
    index=0
    if(index not in list1 and item not in list2):
        return
    return abs(list1[++index]-list2[++index])
list1=[1,2,3,4]
list2=[1,2,3,4]
res=absolute_difference(list1,list2)
