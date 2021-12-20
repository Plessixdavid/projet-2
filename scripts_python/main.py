# coding  : utf-8

import pygame
from game import Game

def Menuconsole():
    print("(1)Nouveaux personnage\t (2)Charger un personnage\t (3)Revenir au bureaux")
    Choixmenu = input("Que voulez vous faire ?")
    if Choixmenu == 1 :
        print("Bienvenu dans ce nouveau monde mais avant d'y acceder j'ai besoin de quelque informations./n ")
        print("Pret? C'est partie allons'y")
        Pseudo = input ("Quelle est votre Pseudo")
        Email = input("quelle est votre email")
        Motdepasse = input("Choisissez un mot de passe")
        print("Je vous remercie , je vous souhaite un bon moment dans ce monde merveilleux. ")
        pygame.init()
        Game().run()
    elif Choixmenu == 2 :
        pass
    elif Choixmenu == 3 :
        exit()




# start code is here
if __name__ == "__main__":
    # Menuconsole()
    print("hello world")
       
    
