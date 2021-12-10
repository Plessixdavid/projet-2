# coding : utf-8

import pygame

# from map import MapManager


# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# FONT = pygame.font.Font("./ressources/dialog_font.ttf", 18)


COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
class input_box:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.font = pygame.font.Font("./ressources/dialog_font.ttf", 18)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.recent_message = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # si l'utilisateur clique sur le rect de la boite de saisie
            if self.rect.collidepoint(event.pos):
                # active la variable ou la desactive si elle est deja active
                self.active = not self.active
            else:
                self.active = False
            # change la couleur actuelle de la boite de saisie si elle est activer/desactiver
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: # envoyer le texte si on presse "enter"
                    # afficher le texte en console pour verifier le fonctionnement
                    print(self.text)
                    # ajouter le message envoyer à la liste de message recent
                    # pour l'afficher ensuite dans le rect qui ce trouve juste au-dessus
                    self.recent_message.append(self.text) 
                    # puis vider la variable qui sert à afficher le texte saisie
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE: # si on appuie sur la touche "retour arriere"
                    # alors supprime le dernier charactere de la str stocker dans la varible "text"
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # renvoyer la saisie du clavier
                self.txt_surface = self.font.render(self.text, True, self.color) # et l'afficher dans le rect de saisie

    def update_chat(self):
        # Redimensionnez la zone si le texte est trop long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw_chat(self, screen):
        # afficher les frappes du clavier
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # afficher le rect de saisie
        pygame.draw.rect(screen, self.color, self.rect, 2)



# def main():
#     # clock = pygame.time.Clock()
#     input_box1 = input_box(100, 100, 140, 32)
#     input_box2 = input_box(100, 300, 140, 32)
#     input_boxes = [input_box1, input_box2]
#     done = False

#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#             for box in input_boxes:
#                 box.handle_event(event)

#         for box in input_boxes:
#             box.update_chat()

#         screen.fill((30, 30, 30))
#         for box in input_boxes:
#             box.draw_chat(screen)

#         pygame.display.flip()
        # clock.tick(30)


# if __name__ == '__main__':
#     main()
#     pygame.quit()