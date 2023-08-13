import pygame
pygame.init()
window_dimensions=[800,800]
flags=pygame.RESIZABLE|pygame.HWSURFACE|pygame.DOUBLEBUF
window=pygame.display.set_mode((window_dimensions[0],window_dimensions[1]),flags)
clock=pygame.time.Clock()
running=True
chessboard_size_8_queens=8
square_size=window_dimensions[0]/chessboard_size_8_queens # this will take the value 100
white=(255,255,255)# this stores the color as an RGB tuple
black=(0,0,0)
def place_object(row,column):
    queen_image=pygame.image.load("D:/Spying_on_The_Queens/Queen.png")
    queen_image=pygame.transform.scale(queen_image,(square_size,square_size-15))
    queen_image=queen_image.convert_alpha()
    queen_image.set_colorkey(white)
    pos_x=column*square_size
    pos_y=row*square_size
    window.blit(queen_image,(pos_x,pos_y))
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
    place_object(4,5)
    # pygame.display.update()
    pygame.display.flip()
pygame.quit()
