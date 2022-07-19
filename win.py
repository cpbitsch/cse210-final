import pygame
import pygame_menu

def win_menu():
    pygame.init()
    surface = pygame.display.set_mode((800,600))

    def restart_the_game():
        # Do the job here !
        start()

    menu = pygame_menu.Menu('Space Invaders', 600, 500, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input("You win!")
    menu.add.button('Play', restart_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)
