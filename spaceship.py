import pygame
import sys
from pygame.locals import *

spaceshipImg = pygame.image.load('spaceship.jpg')


class Spaceship(object):
    def __init__(self, pos):
        self.pos = pos

    def move(self, key):
        if key == 'A':
            if self.pos >= 100:
                self.pos -= 100
        if key == 'D':
            if self.pos < 700:
                self.pos += 100

    def display(self, DISPLAYSURF):
        DISPLAYSURF.blit(spaceshipImg, (self.pos, 700))
