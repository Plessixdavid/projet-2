# Code : utf-8

# Imports :
import pygame

# New function : __init__(self) :
def Windows():
    # Resolution of the screen :
    screen = pygame.display.set_mode((800, 600))     # Double parentheses as a tuple.

    # Title of the game :
    pygame.display.set_caption('Jeu Snake')

    # Color of the screen : black :
    screen.fill((0, 0, 0))

# New function about limits of the screen :      
def create_limits():
    pygame.draw.rect(Windows, (255, 255, 255), (100, 100, 600, 500), 3)
        
