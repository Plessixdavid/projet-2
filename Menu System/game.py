# Coding : utf-8

# Imports :
import pygame 

# Creation of the class Game.
class Game():
    def __init__(self):

        # To have all the fonctionnalities of pygame.
        pygame.init()

        # Variables of menu :
        self.running = True           # When the game is started but not played.
        self.playing = False          # When the player really start the game.
        # All keys are false until the player choose one and become true.
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        # Variables to display the background :
        self.display_width = 800
        self.display_height = 800
        self.display = pygame.surface(self.display_width, self.display_height)
        self.window = pygame.display.set_mode(self.display_width, self.display_height)

        # Font for the menu :
        self.font_name = '8-BIT WONDER.TTF'
        # self.font_name = pygame.font.get_default_font()
        # Colors (RGB) of the font :
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)