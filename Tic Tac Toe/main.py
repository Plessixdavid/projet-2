# Code : utf-8

# Imports:
import pygame
import sys

# New class:
class Game :
    # Function init :
    def __init__(self):
        # Pygame's windows :
        self.ecran = pygame.display.set_mode((600, 600))
        # Name of the game :
        pygame.display.set_caption('Tic Tac Toe')
        # Loop when the game is running :
        self.game_running = True

    # Main function :
    def Main_function(self) :
        # Loop :
        while self.game_running:
            # To receive all elements in pygame :
            for event in pygame.event.get():
                # Quit the game :
                if event.type == pygame.QUIT:
                    sys.exit()

        # Colors of the windows :
        self.ecran.fill((240, 240, 240))

        # Update the screen :
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Game().Main_function()
    pygame.QUIT()