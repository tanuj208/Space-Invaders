import pygame
import sys
import os
from pygame.locals import *
from spaceship import *
from time import time
from alien import *
from missiles import *


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')
BackGround = Background('background.jpg', [0, 0])

font = pygame.font.SysFont('Comic Sans MS', 30, True)

DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)
FPS = 20
score = 0
gameEnd = False

aliens = []
aliens.append(make_alien())
spaceship = Spaceship(100)
missiles = []


def display_images():
    spaceship.display(DISPLAYSURF)
    for alien in aliens:
        if not alien.dead:
            alien.display(DISPLAYSURF)
    for missile in missiles:
        if missile.row >= 0:
            missile.display(DISPLAYSURF)

    DISPLAYSURF.blit(text, (0, 0))


spawn_time = time()

while not gameEnd:

    DISPLAYSURF.fill([0, 0, 0])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)

    for events in pygame.event.get():

        # Alt+F4 or Q to quit game
        if events.type == QUIT:
            pygame.quit()
            gameEnd = True
            break

        if events.type == KEYUP:
            if events.key == K_q:
                pygame.quit()
                gameEnd = True
                break
            if events.key == K_a:
                spaceship.move('A')
            if events.key == K_d:
                spaceship.move('D')
            if events.key == K_SPACE:
                temp = Slow_missile(600, spaceship.pos)
                missiles.append(temp)
            if events.key == K_s:
                temp = Fast_missile(600, spaceship.pos)
                missiles.append(temp)

    if gameEnd:
        break

    # to move missiles in one second interval
    for missile in missiles:
        if time() >= missile.spawn_time+1:
            missile.move()
            missile.spawn_time = time()

    # aliens respawning in 10 seconds
    if time() >= spawn_time+10:
        spawn_time = time()
        aliens.append(make_alien())

    i = 0
    for alien in aliens:
        j = 0
        for missile in missiles:
            if not alien.dead:
                if missile.hit_it(alien.row, alien.col):
                    missile.hit_effect(alien)
                    if missile.type == 1:
                        score += 1
                    missiles.pop(j)
            j += 1

        if not alien.dead and time() >= alien.spawn_time+8:
            alien.dead = True
            aliens.pop(i)
        i += 1

    text = font.render('Score : {0}'.format(
        score), False, (255, 255, 255), (0, 0, 0))
    display_images()

    pygame.display.update()
    fpsClock.tick(FPS)
