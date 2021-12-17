# coding : utf-8

import pygame



COLOR_INACTIVE = pygame.Color(255,255,255)
COLOR_ACTIVE = pygame.Color(255,255,255)
TEXT_COLOR = pygame.Color(255,0,0)

class input_box:

    def __init__(self, text2 = '',text=''):
        self.rect_pseudo = pygame.Rect(608, 437, 320, 32)
        self.rect_mdp = pygame.Rect(605,556, 140, 32)

        self.color = COLOR_INACTIVE
        self.text_color = TEXT_COLOR
        self.pseudo = text
        self.mdp = text2
        self.font = pygame.font.Font("./ressources/dialog_font.ttf", 18)
        self.pseudo_surface = self.font.render(self.pseudo, True, self.text_color)
        self.mdp_surface = self.font.render(self.mdp, True, self.text_color)

        self.pseudo_color = COLOR_INACTIVE
        self.mdp_color = COLOR_INACTIVE
        self.active = False
        self.pseudo_active = False
        self.mdp_active = False
        

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if self.rect_pseudo.collidepoint(event.pos):
                self.pseudo_active = True
                self.mdp_active = False
            elif self.rect_mdp.collidepoint(event.pos):
                self.mdp_active = True
                self.pseudo_active = False
            else:
                self.mdp_active = False
                self.pseudo_active = False
                
            # change la couleur actuelle de la boite de saisie si elle est activer/desactiver
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: # envoyer le texte si on presse "enter"
                    # afficher le texte en console pour verifier le fonctionnement
                    print(self.pseudo)
                    
                    # ajouter le message envoyer à la liste de message recent
                    # pour l'afficher ensuite dans le pseudo qui ce trouve juste au-dessus
                    # puis vider la variable qui sert à afficher le texte saisie
                    
                elif event.key == pygame.K_BACKSPACE: # si on appuie sur la touche "retour arriere"
                    # alors supprime le dernier charactere de la str stocker dans la variable "text"
                    if self.pseudo_active:
                    # get text input from 0 to -1 i.e. end.
                        self.pseudo = self.pseudo[:-1]
                    if self.mdp_active:
                        self.mdp = self.mdp[:-1]
                    
                else:
                    if self.pseudo_active:
                        self.pseudo += event.unicode
                    if self.mdp_active:
                        self.mdp += event.unicode
                    
                # renvoyer la saisie du clavier
                # self.txt_surface = self.font.render(self.pseudo, True, self.text_color) # et l'afficher dans le pseudo de saisie
                self.pseudo_surface = self.font.render(self.pseudo, True, (255, 255, 255))
                self.mdp_surface2 = self.font.render(self.mdp, True, (255, 255, 255))
    def update_chat(self):
        # Redimensionnez la zone si le texte est trop long.
        pseudo_width = max(320, self.pseudo_surface.get_width()+10)
        pseudo_height = max(32, self.pseudo_surface.get_height()+10)
        self.rect_pseudo_w = pseudo_width
        self.rect_pseudo_h = pseudo_height
        mdp_width = max(320, self.pseudo_surface.get_width()+10)
        mdp_height = max(32, self.pseudo_surface.get_height()+10)
        self.rect_mdp_w = mdp_width
        self.rect_mdp_h = mdp_height

    def draw_chat(self, screen):
        # afficher les frappes du clavier
        screen.blit(self.pseudo_surface, (self.rect_pseudo_w+5, self.rect_pseudo_h+5))
        screen.blit(self.mdp_surface, (self.rect_mdp_w+5, self.rect_mdp_h+5))
        # afficher le rect de saisie

        pygame.draw.rect(screen, self.pseudo_color, self.rect_pseudo, 4)
        pygame.draw.rect(screen, self.mdp_color, self.rect_mdp , 4)
        
