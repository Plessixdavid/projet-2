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
                # Event : right click : 
                    # [0] : list of buttons in the mouse = right click. 
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:   
                    # Get the position of the mouse :
                    position = pygame.mouse.get_pos()
                    # Position x of the mouse :
                    position_x = position[0]//200
                    # Position y of the mouse :
                    position_y = position[1]//200
                    
                    print(position_x, position_y)
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