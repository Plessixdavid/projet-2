# Code : utf-8

# Imports :
import pygame
from menu.Snake_Game.game import Game4

# New function : main :
def Snake_start():
    pygame.init()
    Game4().Main_function()
    pygame.quit()

if __name__ == '__main__':
    Snake_start()