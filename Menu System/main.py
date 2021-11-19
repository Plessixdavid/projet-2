# Coding : utf-8

# Imports :
import pygame
from game import game

# Attribution of the function Game :
g = game()

# Loop when the game is running :
while g.running:
    pygame.init()
    g.playing = True
    g.game_loop()