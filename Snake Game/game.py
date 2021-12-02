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

        # Variable about the body of the snake :
        self.snake_body = 10

        # Position of the apple :
        self.apple_position_x = random.randrange(110, 690, 10)
        self.apple_position_y = random.randrange(110, 590, 10)
        # Position at the beginning :
        self.apple = 10

        # Stare FPS :
        self.clock = pygame.time.Clock()

        # List that will store all snake's positions :
        self.positions_snake = []

        

    # New function : Main_function :
    def Main_function(self):
        # Loop when the game is running : 
        while self.game_running:

            # Loop to verify the event :
            for evenement in pygame.event.get():
                # Close the windows :
                if evenement.type == pygame.QUIT:
                    sys.exit()
                
                # Events for the direction of the snake :
                # Event KEYDOWN :
                if evenement.type == pygame.KEYDOWN:
                    # Event K_RIGHT :
                    if evenement.key == pygame.K_RIGHT:
                        self.snake_direction_x = 10
                        self.snake_direction_y = 0
                    # Event K_LEFT :
                    if evenement.key == pygame.K_LEFT:
                        self.snake_direction_x = -10
                        self.snake_direction_y = 0
                    # Event K_DOWN :
                    if evenement.key == pygame.K_DOWN:
                        self.snake_direction_y = 10
                        self.snake_direction_x = 0
                    # Event K_UP :
                    if evenement.key == pygame.K_UP:
                        self.snake_direction_y = -10
                        self.snake_direction_x = 0

            # Condition if the snake is out the limits of the rectangle :
            if (self.snake_position_x <= 100) or (self.snake_position_x >= 700) \
                or (self.snake_position_y <= 100) or (self.snake_position_y >= 600) :
                self.game_running = False

            # Condition if the snake eats the apple :
            if self.apple_position_y == self.snake_position_y and self.snake_position_x == self.apple_position_x:
                self.apple_position_x = random.randrange(110,690,10)
                self.apple_position_y = random.randrange(110,590,10)                
                
                # Increase the height of the snake +1 :
                self.height_body_snake += 1
                
                # Increase the score of the player +1 :
                self.score += 1

            # Limits of the game in the screen :
            create_limits()

            # Speed initial of the snake :
            self.clock.tick(10)
            self.speed_snake()

            # List that will store the snake's position :
            head_snake = []
            head_snake.append(self.serpent_position_x)
            head_snake.append(self.serpent_position_y)

            # Update the screen :     
            pygame.display.flip()

    # New function about movements of the snake :       
    def snake_movement(self):
        # Make the snake moves at right or at left on the screen :
        self.snake_position_x += self.snake_direction_x
        # Make the snake moves at up or at down on the screen :
        self.snake_position_y += self.snake_direction_y  

    # New function : display differents elements : 
    def display_elements(self):
        # Display the snake :
        # Windows.blit(self.image_snake_head,(self.snake_position_x, self.snake_position_y, self.snake_body, self.snake_body))
        # Display the apple (color : red) :
        pygame.draw.rect(Windows, (255, 0, 0), (self.apple_position_x, self.apple_position_y, self.apple, self.apple))

    # New function : increase the speed of the snake following his height :
    def speed_snake(self):
        if self.height_body_snake > 5:
            self.clock.tick(20)
        elif self.height_body_snake > 10:
            self.clock.tick(30)
        elif self.height_body_snake > 20:
            self.clock.tick(40)
        elif self.height_body_snake > 30:
            self.clock.tick(50)