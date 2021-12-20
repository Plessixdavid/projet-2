# coding : utf-8

import pygame
from animation import animate_sprite

COLOR_INACTIVE = pygame.Color(175, 175 ,175)
COLOR_ACTIVE = pygame.Color(255, 0, 0)
TEXT_COLOR = pygame.Color(48, 48, 48)

class chat_box:

    def __init__(self, text='', sio=None):
        self.rect = pygame.Rect(10, 720, 220, 32)
        self.rect_2 = pygame.Rect(10, 597, 220, 120)
        self.color = COLOR_INACTIVE
        self.color_text = TEXT_COLOR
        self.sio = sio
        self.color_fill_off = 60
        self.color_fill_on = 200
        self.color_fill = self.color_fill_off
        self.text = text
        self.messages = ["", "", ""]
        self.recent_message = ''
        self.font = pygame.font.Font("./ressources/dialog_font.ttf", 15)
        self.txt_surface = self.font.render(self.text, True, self.color_text)
        self.mess_surface = self.font.render(self.messages[0], True, self.color_text)
        self.mess_surface_1 = self.font.render(self.messages[1], True, self.color_text)
        self.mess_surface_2 = self.font.render(self.messages[2], True, self.color_text)
        self.active = False

        # GET All the chat ! And update the chat on new messages
        if sio is not None:
            @self.sio.on('MESSAGE')
            def message(data):
                self.messages =  data
            
            self.sio.emit("GET CHAT")

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
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: # envoyer le texte si on presse "enter"
                    # afficher le texte en console pour verifier le fonctionnement
                    print(self.text)
                    # self.mess_surface = self.font.render(self.recent_message, True, self.color_text)
                    self.messages.append(self.text)
                    # ajouter le message envoyer à la liste de message recent
                    if len(self.messages) > 3:
                        self.messages.pop(0)

                    self.mess_surface = self.font.render(f"{animate_sprite.firstnane} dit: {self.messages[0]}", True, self.color_text)
                    self.mess_surface_1 = self.font.render(f"{animate_sprite.firstnane} dit: {self.messages[1]}", True, self.color_text)
                    self.mess_surface_2 = self.font.render(f"{animate_sprite.firstnane} dit: {self.messages[2]}", True, self.color_text)
                    print(self.messages)
                    # pour l'afficher ensuite dans le rect qui ce trouve juste au-dessus
                    print(self.recent_message)
                    # puis vider la variable qui sert à afficher le texte saisie
                    # Send message to the server
                    if self.sio is not None:
                        self.sio.emit('NEW MESSAGE', f"{animate_sprite.firstnane} dit: {self.recent_message}")
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
                self.txt_surface = self.font.render(self.text, True, self.color_text) # et l'afficher dans le rect de saisie

    def update_chat(self):
        # Redimensionnez la zone si le texte est trop long.
        width = max(320, self.txt_surface.get_width()+10)
        height = max(32, self.txt_surface.get_height()+10)
        self.rect.w = width
        self.rect.h = height

    def draw_chat(self, screen):
        # afficher le rect de saisie
        color_rect = pygame.Surface((self.rect.w-1.5, self.rect.h-1.5), pygame.SRCALPHA)
        color_rect.fill((175, 175, 175, self.color_fill))
        color_rect_2 = pygame.Surface((self.rect_2.w-1, self.rect_2.h-1), pygame.SRCALPHA)
        color_rect_2.fill((175, 175, 175, self.color_fill))
        pygame.draw.rect(screen, self.color, self.rect, 4)
        pygame.draw.rect(screen, self.color, self.rect_2, 3)
        # afficher les frappes du clavier
        screen.blit(color_rect, (self.rect.x+1, self.rect.y+1))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(color_rect_2, (self.rect_2.x+1, self.rect_2.y+1))
        screen.blit(self.mess_surface, (self.rect_2.x+5, self.rect_2.y+5))
        screen.blit(self.mess_surface_1, (self.rect_2.x+5, self.rect_2.y+25))
        screen.blit(self.mess_surface_2, (self.rect_2.x+5, self.rect_2.y+45))
        # 1er essai pour rendre le rect du chat transparent
        #s = pygame.Surface((self.rect_2.w,self.rect_2.h), pygame.SRCALPHA, )   # per-pixel alpha
        #s.fill((175,175,175,128))                         # notice the alpha value in the color
        #screen.blit(s, (self.rect_2.x, self.rect_2.y))
