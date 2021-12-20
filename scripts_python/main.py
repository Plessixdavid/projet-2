# coding  : utf-8

import pygame
from game import Game


# start code is here
if __name__ == "__main__":
    pseudo = input("Votre pseudo?\n")
    mail = input("Votre adresse mail?\n")
    mdp = input("Votre mot de passe?\n")
    if pseudo != None and mail != None and mdp != None:
        pygame.init()
        Game(pseudo=pseudo).run()   
    
