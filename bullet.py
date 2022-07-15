import pygame
import math
import constants

class Bullet():

    def __init__(self):

        self._bullet_image = pygame.image.load('data/bullet.png')
        self._bullet_X = 0
        self._bullet_Y = 500
        self._Xchange = 0
        self._Ychange = 3
        self._state = "rest"

    def isCollision(self, x1, x2, y1, y2):
        distance = math.sqrt((math.pow(x1 - x2,2)) +
                            (math.pow(y1 - y2,2)))
        if distance <= 50:
            return True
        else:
            return False

    def bullet(self, x, y):
        global bullet_state
        constants.SCREEN.blit(self._bullet_image, (x, y))
        self._state = "fire"
