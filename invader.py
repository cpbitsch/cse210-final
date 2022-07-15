import pygame
import random
import constants

class Invader():

    def __init__(self):

        self._invader_image = []
        self._invader_X = []
        self._invader_Y = []
        self._Xchange = []
        self._Ychange = []
        self._no_of_invaders = 8

    
    def populate_invaders(self):
        for num in range(self._no_of_invaders):
            self._invader_image.append(pygame.image.load('data/alien.png'))
            self._invader_X.append(random.randint(64, 737))
            self._invader_Y.append(random.randint(30, 180))
            self._Xchange.append(1.2)
            self._Ychange.append(50)

    def invader(self, x, y, i):
        constants. SCREEN.blit(self._invader_image[i], (x, y))
