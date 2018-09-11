import pygame
import sys
from pygame.locals import *
from time import time
from random import randint

alien_spawn_time = 0
alien_present = 0
alienImg = pygame.image.load('alien.png')
hitImg = pygame.image.load('trapped.jpg')


class Alien(object):
    def __init__(self):
        self.row = randint(0, 1)*100
        self.col = randint(0, 7)*100
        self.freeze = False
        self.dead = False
        self.spawn_time = 0

    def kill(self):
        self.dead = True

    def freezed(self):
        self.freeze = True
        self.spawn_time = time()-3

    def display(self, DISPLAYSURF):
        if self.freeze:
            DISPLAYSURF.blit(hitImg, (self.col, self.row))
        else:
            DISPLAYSURF.blit(alienImg, (self.col, self.row))


def make_alien():
    alien = Alien()
    alien.spawn_time = time()
    return alien
