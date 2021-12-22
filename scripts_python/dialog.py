# coding : utf-8

import pygame

class dialog_box:
    """
    boite de dialogue des PNJs
    """
    def __init__(self): # sans commentaire
        self.box = pygame.image.load("./ressources/png/boite_de_dialogue.png")
        self.box = pygame.transform.scale(self.box, (700, 90)) # selectionne une image et modifie ses dimentions
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("./ressources/dialog_font.ttf", 12)
        self.reading = False

    def execute(self, dialog=[]):
        """
        utilise la fonction 'change_text' en complément.
        permet d'enclencher la boite de dialogue et le changement de texte sur commande
        et de remettre la valeur 'text_index' à zéro quand la boite de dialogue est désactivée
        """
        if self.reading:
            self.change_text()

        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog

    def render(self, screen):
        """
        affiche ou enlève la boite de dialogue
        - affiche si il n'y a pas déjà une boite de dialogue en cours
        - enlève si le texte du PNJ est terminé
        """
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box, (0, 0))
            text = self.font.render(self.texts[self.text_index], False, (0, 0, 0))
            screen.blit(text, (25, 15))

    def change_text(self):
        """
        passe les textes de la liste de dialogue du PNJ
        du premier au dernier
        """
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False