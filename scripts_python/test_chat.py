# coding : utf-8

import pygame
from animation import animate_sprite

COLOR_INACTIVE = pygame.Color(175, 175 ,175)
COLOR_ACTIVE = pygame.Color(48, 48, 48)
class input_box:

    def __init__(self, text=''):
        self.rect = pygame.Rect(1000, 320, 320, 32)
        self.rect_2 = pygame.Rect(1000, 0, 320, 320)
        
        self.color = COLOR_INACTIVE
        self.text = text
        self.recent_message = ''
        self.font = pygame.font.Font("./ressources/dialog_font.ttf", 12)
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.mess_surface = self.font.render(self.recent_message, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # si l'utilisateur clique sur le rect de la boite de saisie
            if self.rect.collidepoint(event.pos):
                # active la saisie ou la desactive si elle est deja active
                self.active = not self.active
            else:
                self.active = False
            # change la couleur actuelle de la boite de saisie si elle est activer/desactiver
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: # envoyer le texte si on presse "enter"
                    # afficher le texte en console pour verifier le fonctionnement
                    self.mess_surface = self.font.render(f"{animate_sprite.firstnane} dit: {self.recent_message}", True, self.color)
                    # ajouter le message envoyer à la liste de message recent
                    # pour l'afficher ensuite dans le rect qui ce trouve juste au-dessus
                    # puis vider la variable qui sert à afficher le texte saisie
                    self.text = ''
                    self.recent_message = ''
                elif event.key == pygame.K_BACKSPACE: # si on appuie sur la touche "retour arriere"
                    # alors supprime le dernier charactere de la str stocker dans la variable "text"
                    self.text = self.text[:-1]
                    self.recent_message = self.recent_message[:-1]
                else:
                    self.text += event.unicode
                    self.recent_message += event.unicode
                # renvoyer la saisie du clavier
                self.txt_surface = self.font.render(self.text, True, self.color) # et l'afficher dans le rect de saisie

    def update_chat(self):
        # Redimensionnez la zone si le texte est trop long.
        width = max(320, self.txt_surface.get_width()+10)
        height = max(32, self.txt_surface.get_height()+10)
        self.rect.w = width
        self.rect.h = height

    def draw_chat(self, screen):
        # afficher les frappes du clavier
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(self.mess_surface, (self.rect_2.x+5, self.rect_2.y+5))
        # afficher le rect de saisie
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.draw.rect(screen, self.color, self.rect_2, 2)
