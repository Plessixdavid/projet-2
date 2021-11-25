# Code : utf-8

# Imports:
import pygame
import sys

class Jeu :
    def __init__(self):
        self.ecran = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Tic Tac Toe')
        self.game_running = True

    