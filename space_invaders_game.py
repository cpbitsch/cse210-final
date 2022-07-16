import pygame
import random
import math
from pygame import mixer

import constants

from score import Score
from player import Player
from invader import Invader
from bullet import Bullet

import win

import space_invaders_game


def start():
    pygame.init()
    GAME_OVER_FONT = pygame.font.Font('freesansbold.ttf', 64)


    score = Score()
    player = Player()
    invader = Invader()
    bullet = Bullet()

    invader.populate_invaders()


    game_over_font = pygame.font.Font('freesansbold.ttf', 64)
    def game_over():
        game_over_text = game_over_font.render("GAME OVER",
                                            True, (255,0,0))
        screen.blit(game_over_text, (190, 250))
        restart_text_font = pygame.font.Font('freesansbold.ttf', 20)
        restart_text = restart_text_font.render("PRESS R to Play again...",
                                            True, (0,102,0))
        screen.blit(restart_text, (270, 350))  

    screen = constants.SCREEN

    pygame.display.set_caption("Welcome to Space\
    Invaders Game by:- styles")

    mixer.music.load('data/background.wav')
    mixer.music.play(-1)

    running = True
    while running:

        constants.CLOCK.tick(500)


        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                mixer.music.unload()
                break


            if event.type == pygame.KEYDOWN:
                ## Code for restarting the game
                if event.key == pygame.K_r:
                    space_invaders_game.start()
                if event.key == pygame.K_LEFT:
                    player._Xchange = -1.7
                if event.key == pygame.K_RIGHT:
                    player._Xchange = 1.7
                if event.key == pygame.K_SPACE:
                
                    if bullet._state is "rest":
                        bullet._bullet_X = player._player_X
                        bullet.bullet(bullet._bullet_X, bullet._bullet_Y)
                        bullet_sound = mixer.Sound('data/bullet.wav')
                        bullet_sound.play()
            if event.type == pygame.KEYUP:
                player._Xchange = 0

        player._player_X += player._Xchange
        for i in range(invader._no_of_invaders):
            invader._invader_X[i] += invader._Xchange[i]

        if bullet._bullet_Y <= 0:
            bullet._bullet_Y = 600
            bullet._state = "rest"
        if bullet._state == "fire":
            bullet.bullet(bullet._bullet_X, bullet._bullet_Y)
            bullet._bullet_Y -= bullet._Ychange

        for i in range(invader._no_of_invaders):
            
            if invader._invader_Y[i] >= 450:
                if abs(player._player_X-invader._invader_X[i]) < 80:
                    for j in range(invader._no_of_invaders):
                        invader._invader_Y[j] = 2000
                        explosion_sound = mixer.Sound('data/explosion.wav')
                        explosion_sound.play()
                    mixer.music.unload()
                    game_over()
                    break

            if invader._invader_X[i] >= 735 or invader._invader_X[i] <= 0:
                invader._Xchange[i] *= -1
                invader._invader_Y[i] += invader._Ychange[i]

            collision = bullet.isCollision(bullet._bullet_X, invader._invader_X[i], bullet._bullet_Y, invader._invader_Y[i])
            if collision:
                score._score_val += 1
                bullet._bullet_Y = 600
                bullet._state = "rest"
                invader._invader_X[i] = random.randint(64, 736)
                invader._invader_Y[i] = random.randint(30, 200)
                invader._Xchange[i] *= -1

            invader.invader(invader._invader_X[i], invader._invader_Y[i], i)


        if player._player_X <= 16:
            player._player_X = 16
        elif player._player_X >= 750:
            player._player_X = 750

        if score._score_val == 25:
            mixer.music.unload()
            
            win.win_menu()
            
            pygame.quit()
            quit()

        player.player(player._player_X, player._player_Y)
        score.show_score(score._scoreX, score._scoreY)
        pygame.display.update()

# start()