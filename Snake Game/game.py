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
        # Resolution of the screen :
        self.screen = pygame.display.set_mode((800, 600))     # Double parentheses as a tuple.
        # Title of the game :
        pygame.display.set_caption('Jeu Snake')

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

        # Variable about the height of the snake :
        self.height_body_snake = 1

        # Variable for the screen of the beginning :
        self.screen_beginning = True

        # Charge image :
        self.head_snake = pygame.image.load('Snake Game/head_snake.png')
        self.image = pygame.image.load('snake-game.jpg')
        # Shrink the image :
        self.image_title = pygame.transform.scale(self.image, (200, 100))

        # Variable score :
        self.score = 0
        
    # New function : Main_function :
    def Main_function(self):

        # Loop for the screen of beginning :
        while self.screen_beginning:
            # Loop to verify the event :
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.screen_beginning = False

                self.screen.fill((0, 0, 0))

                # Display the image of the title in a rectangle :
                self.screen.blit(self.image_title, (300, 50, 100, 50))

                # Messages :
                self.create_message('small', 'Le but du jeu est que le serpent se développe.', (250, 200, 200, 5), (240, 240, 240))
                self.create_message('small',' Pour cela, il a besoin de pommes. Mangez-en autant que possible pour grandir !!', (190, 220, 200, 5), (240, 240, 240))
                self.create_message('medium','Appuyer sur Enter pour commencer.', (200, 450, 200, 5), (255, 255, 255))                
                
                pygame.display.flip()
    
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

            # Movements of the snake :
            self.snake_movement()

            # Condition if the snake eats the apple :
            if self.apple_position_y == self.snake_position_y and self.snake_position_x == self.apple_position_x:
                self.apple_position_x = random.randrange(110, 690, 10)
                self.apple_position_y = random.randrange(110, 590, 10)                
                
                # Increase the height of the snake +1 :
                self.height_body_snake += 1
                
                # Increase the score of the player +1 :
                self.score += 1

            # List that will store the snake's head position :
            head_snake = []
            head_snake.append(self.snake_position_x)
            head_snake.append(self.snake_position_y)

            # Append snake's head positions in the list of snake positions : 
            self.positions_snake.append(head_snake)

            # Condition to resolve about the height of the snake through his position :
            if len(self.positions_snake) > self.height_body_snake :
                # We use .pop to delete the initial position of the snake.
                self.positions_snake.pop(0)

            # Display elements :
            self.display_elements()

            # Display the function bite_him :
            self.bite_him()

            # Display the title and the score :
            self.create_message('big', 'Snake Game', (320, 10, 100, 50), (255, 255, 255))
            self.create_message('big','{}'.format(str(self.score)), (375, 50, 50, 50), (255, 255, 255))

            # Limits of the game in the screen :
            self.create_limits()

            # Speed initial of the snake :
            self.clock.tick(10)
            self.speed_snake()

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
        # Color of the screen : black :
        self.screen.fill((0, 0, 0))

        # Display the snake (color : green) :
        pygame.draw.rect(self.screen, (0, 250, 0), (self.snake_position_x, self.snake_position_y, self.snake_body, self.snake_body))
        # self..blit(self.image_snake_head,(self.snake_position_x, self.snake_position_y, self.snake_body, self.snake_body))

        # Display the apple (color : red) :
        pygame.draw.rect(self.screen, (255, 0, 0), (self.apple_position_x, self.apple_position_y, self.apple, self.apple))

        # Display parts of the snake :
        self.display_elements()

    # New function : display the snake :
    def display_snake(self):
        # Display all parts of the snake :
        for parts_of_snake in self.positions_snake[:-1]:
            pygame.draw.rect(self.screen, (0, 255, 0), (parts_of_snake[0], parts_of_snake[1], self.body_snake, self.body_snake))
        
    # New function when the snake bite his end : 
    def bite_him(self,head_snake):
        # We said self.positions_snake[:-1] because he can't bite his head.
        for part_snake in self.positions_snake[:-1]:
            if part_snake == head_snake :
                self.game_running = False

    # New function to create messages :
    def create_message(self, font, message, message_rectangle, color):
        if font == 'small':
            font = pygame.font.SysFont('Lato', 20 ,False)
        elif font == 'medium':
            font = pygame.font.SysFont('Lato', 30 ,False)
        elif font == 'big':
            font = pygame.font.SysFont('Lato', 40 , True)
        
        # Variable to display the text :
        message = font.render(message, True, color)
        # Display on the screen :
        self.screen.blit(message, message_rectangle)

    def create_limits(self):
        pygame.draw.rect(Windows, (255, 255, 255), (100, 100, 600, 500), 3)

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
   