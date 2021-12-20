# coding : utf-8

"""
    test d'amélioration
"""

import pygame

COLOR_INACTIVE = pygame.Color(175, 175 ,175)
COLOR_ACTIVE = pygame.Color(255, 0, 0)
TEXT_COLOR = pygame.Color(48, 48, 48)

class input_box:

    def __init__(self, x=0, y=0, w=96, h=32, color_active=COLOR_ACTIVE, color_inactive=COLOR_INACTIVE, color_text=TEXT_COLOR, font_size=15, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color = self.color_inactive
        self.color_text = color_text
        self.color_fill_off = 75
        self.color_fill_on = 200
        self.color_fill = self.color_fill_off
        self.text = text
        self.font = pygame.font.Font("./ressources/dialog_font.ttf", font_size)
        self.txt_surface = self.font.render(self.text, True, self.color_text)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos) # pour avoir la position de la souris quand on clique
            # si l'utilisateur clique sur le rect de la boite de saisie
            if self.rect.collidepoint(event.pos):
                # active la saisie ou la desactive si elle est deja active
                self.active = not self.active
            else:
                self.active = False
                self.color_fill = self.color_fill_off
            # change la transparence si la boite est active
            if self.active:
                self.color_fill = self.color_fill_on
            else:
                self.color_fill = self.color_fill_off
            # change la couleur actuelle de la boite de saisie si elle est activer/desactiver
            self.color = self.color_active if self.active else self.color_inactive
            
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: # envoyer le texte si on presse "enter"
                    # afficher le texte en console pour verifier le fonctionnement
                    print(self.text)
                    # ajouter le message envoyer à la liste de message recent
                    # pour l'afficher ensuite dans le rect qui ce trouve juste au-dessus
                    # puis vider la variable qui sert à afficher le texte saisie
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE: # si on appuie sur la touche "retour arriere"
                    # alors supprime le dernier charactere de la str stocker dans la variable "text"
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # renvoyer la saisie du clavier
                self.txt_surface = self.font.render(self.text, True, self.color_text) # et l'afficher dans le rect de saisie

    def update_chat(self):
        """
            optionnel
            pour redimensionnez la zone de saisie si le texte est trop long.
        """
        width = max(320, self.txt_surface.get_width()+10)
        height = max(32, self.txt_surface.get_height()+10)
        self.rect.w = width
        self.rect.h = height

    def draw_chat(self, screen):
        # afficher le rect de saisie
        pygame.draw.rect(screen, self.color, self.rect, 3)
        # afficher les frappes du clavier
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))


# input_box(x=100, y=700, w=120, h=32)