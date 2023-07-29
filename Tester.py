import pygame
pygame.init()
window_dimensions=[400,400]
flags=pygame.RESIZABLE|pygame.HWSURFACE|pygame.DOUBLEBUF
window=pygame.display.set_mode((window_dimensions[0],window_dimensions[1]),flags)
pygame.quit()