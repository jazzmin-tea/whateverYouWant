import pygame
from engine import terminal
import random as rnd
import numpy as np
import math
import time


def main():

    pygame.font.init()

    FPS = 30
    run = True
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = 800, 800
    wd = r'C:\Users\logan\OneDrive\Documents'

    t = terminal(wd, HEIGHT, WIDTH)

    pygame.display.set_caption('terminal')

    while run:
        clock.tick(FPS)
        for event in pygame.event.get(eventtype=pygame.QUIT):
            if event.type == pygame.QUIT:  # quit if user quits
                run = False

        t.get_pressed()
        t.draw()


if __name__ == '__main__':
    main()
    pygame.quit()

