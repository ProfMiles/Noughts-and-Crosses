import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Noughts and Crosses")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()