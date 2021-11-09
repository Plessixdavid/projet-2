# coding: utf-8

#Créer une classe pour notre jeu.
from Player import Player


class Game:

    def __init__(self):
        #Générer joueur quand parti débute.
        self.player = Player()