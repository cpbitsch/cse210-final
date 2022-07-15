import pygame
import constants

class Player():

    def __init__(self):
        
        self._player_image = pygame.image.load('data/spaceship.png')
        self._player_X = 370
        self._player_Y = 523
        self._Xchange = 0

    def player(self, x, y):
        constants.SCREEN.blit(self._player_image, (x - 16, y + 10))
