# Code : utf-8

# Imports:
import pygame
from background import *
from game import *

def main():
    pygame.init()
    Game().Main_function()
    pygame.quit() 

if __name__ == '__main__':
    main()