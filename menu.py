import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800,600))

def start_the_game():
    # Do the job here !
    pass

def help_menu():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Space Invaders', 600, 500,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Input Name :', default='')
menu.add.button('Play', start_the_game)
menu.add.button('Help', help_menu)
menu.add.button('Quit', pygame_menu.events.EXIT)
