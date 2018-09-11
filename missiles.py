import pygame
import sys
from pygame.locals import *
from time import time

missileImg = pygame.image.load('missile2.png')
missileImg2 = pygame.image.load('missile.png')


class Missile(object):
    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.spawn_time = time()


class Slow_missile(Missile, object):
    type = 1
    speed = 100

    def __init__(self, row, col):
        Missile.__init__(self, row, col)

    def move(self):
        self.row -= self.speed

    def hit_effect(self, alien):
        alien.kill()

    def display(self, DISPLAYSURF):
        DISPLAYSURF.blit(missileImg2, (self.col, self.row))

    def hit_it(self, alien_row, alien_col):
        if alien_row == self.row and alien_col == self.col:
            return True


class Fast_missile(Missile, object):
    type = 2
    speed = 200

    def __init__(self, row, col):
        Missile.__init__(self, row, col)

    def move(self):
        self.row -= self.speed

    def hit_effect(self, alien):
        alien.freezed()

    def display(self, DISPLAYSURF):
        DISPLAYSURF.blit(missileImg, (self.col, self.row))

    def hit_it(self, alien_row, alien_col):
        if (alien_row == self.row or alien_row == self.row+100):
            if alien_col == self.col:
                return True
