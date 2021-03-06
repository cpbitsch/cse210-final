import pygame
import pygame_menu
import space_invaders_game


pygame.init()
surface = pygame.display.set_mode((800,600))

def start_the_game():
    # Do the job here !
    space_invaders_game.start()

def help_menu():
    # Do the job here !
    menu = pygame_menu.Menu('Space Invaders', 600, 500, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.label('Space to fire')
    menu.add.label('Left and Right arrow keys to move')
    menu.add.button('Back', main)

    menu.mainloop(surface)

def main():
    menu = pygame_menu.Menu('Space Invaders', 600, 500, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input("Welcome to Space Invaders")
    menu.add.button('Play', start_the_game)
    menu.add.button('Help', help_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)

main()