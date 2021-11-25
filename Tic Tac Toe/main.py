# Code : utf-8

# Imports:
import pygame
import sys
from grid import *

# New class:
class Game :
    # Function init :
    def __init__(self):
        # Pygame's windows :
        self.screen = pygame.display.set_mode((600, 600))
        # Name of the game :
        pygame.display.set_caption('Tic Tac Toe')
        # Loop when the game is running :
        self.game_running = True
        self.grids = Grid(self.screen)

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
            self.screen.fill((240, 240, 240))

            # Display the lines of the grids :
            self.grids.display_lines()

            # Update the screen :
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Game().Main_function()
    pygame.QUIT()