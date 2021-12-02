# Code : utf-8

# Imports :
import pygame

# New class : Windows :
class Windows :
    # New function : __init__(self) :
    def __init__(self):
        # Resolution of the screen :
        self.screen = pygame.display.set_mode((800, 600))     # Double parentheses as a tuple.
        