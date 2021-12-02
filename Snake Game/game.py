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
        # Class Screen of the file screen :
        Windows()

        # Variable : game_running : 
        self.game_running = True

        # Position of the snake :
            # Initial position of the snake in the screen :
        self.snake_position_x = 300
        self.snake_position_y = 300
        # Position for the direction of the snake : 
        self.snake_direction_x = 0
        self.snake_direction_y = 0

    # New function : Main_function :
    def Main_function(self):
        # Loop when the game is running : 
        while self.game_running:

            # Loop to verify the event :
            for evenement in pygame.event.get():
                # Close the windows :
                if evenement.type == pygame.QUIT:
                    sys.exit()
                    
                # Event KEYDOWN :
                if evenement.type == pygame.KEYDOWN:
                    # Event K_RIGHT :
                    if evenement.key == pygame.K_RIGHT:
                        self.snake_direction_x = 10
                        self.snake_direction_y = 0
                    # Event K_LEFT :
                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                    # Event K_DOWN :
                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0
                    # Event K_UP :
                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0
        
            # Update the screen :     
            pygame.display.flip()