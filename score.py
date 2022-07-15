import pygame
import constants

class Score():

    def __init__(self):
        self._score_val = 0
        self._scoreX = 5
        self._scoreY = 5
        self._font = pygame.font.Font('freesansbold.ttf', 20)

    def show_score(self, x, y):
        score = self._font.render("Points: " + str(self._score_val), True, (255,255,255))
        constants.SCREEN.blit(score, (x , y ))
