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
        self.playing = False          # When the player really gamed.
        # All keys are false until the player choose one and become true.
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        # Variables to display the background :
        self.display_width_min = 800
        self.display_width_max = 1980
        self.display_height_min = 800
        self.display_height_max = 1080
        self.display = pygame.surface(self.display_width_min, self.display_height_min)
        self.window = pygame.display.set_mode(self.display_width_min, self.display_height_min)

       