import pygame
from pygame.locals import *


pygame.init()
display = (800,600)
screen = pygame.display.set_mode(display)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(pygame.Color("#191529"))
    
    pygame.display.flip()
