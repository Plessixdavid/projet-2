# coding  : utf-8

import pygame
from game import Game
from BDD.DBUtil import DBUtil
import itertools
import var as var
def Menuconsole():

    Pseudo = ""
    print("(1)Nouveaux personnage\t (2)Charger un personnage\t (3)Revenir au bureaux")
    Choixmenu = input("Que voulez vous faire ?")
    if Choixmenu == "1" :
        print("Bienvenu dans ce nouveau monde mais avant d'y acceder j'ai besoin de quelque informations./n ")
        print("Pret? C'est partie allons'y")

        var.Pseudo = input ("Quelle est votre Pseudo")
        var.Email = input("quelle est votre email")
        var.Motdepasse = input("Choisissez un mot de passe")
        print("Je vous remercie , je vous souhaite un bon moment dans ce monde merveilleux. ")
        Query = "INSERT INTO data_joueur (mot_de_passe, email, Name ) VALUES (%s, %s, %s)"
        Values = (var.Motdepasse, var.Email, var.Pseudo)
        DBUtil.ExecuteQuery(Query, Values)
        

    elif Choixmenu == "2" :
        answer = False
        while answer == False:
            var.Pseudo = input("pseudo:")
            var.Motdepasse = input("mot de passe:")
            list = DBUtil.ExecuteQuery("SELECT * FROM data_joueur")
            print(list)
            
            if (var.Pseudo in itertools.chain(*list) and var.Motdepasse in itertools.chain(*list)):
                print(f"bienvenu {Pseudo}" )
                
                answer = True
            else:
                print("mot de passe ou pseudo incorrect.")
                              
            
    elif Choixmenu == "3" :
        exit()




# start code is here
if __name__ == "__main__":
    Menuconsole()
    pygame.init()
    Game().run()
    
    
