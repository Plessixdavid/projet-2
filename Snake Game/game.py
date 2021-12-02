# Code : utf-8

# Imports :
import pygame
import sys
import random
from screen import *

# New class : Game :
class Game :
    # New function : __init__(self) :
    def __init__(self):
        # Class Windows of the file screen :
        Windows()

        # Variable : game_running : 
        self.game_running = True

    # New function : Main_function :
    def Main_function(self):
        # Loop when the game is running : 
        while self.game_running:
            # Loop to verify the event :
            for evenement in pygame.event.get():
                # Close the windows :
                if evenement.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            