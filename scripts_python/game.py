# coding : utf-8

import pygame
from map import MapManager
from player import Player
from dialog import dialog_box
from player_chat import chat_box, COLOR_ACTIVE, COLOR_INACTIVE, TEXT_COLOR
from input_box import input_box

class Game:

    def __init__(self):
        # créer la fenetre du jeu
        self.screen = pygame.display.set_mode((900,780))
        pygame.display.set_caption("PYGAMON")

        self.font = pygame.font.Font("./ressources/dialog_font.ttf", 18)

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = dialog_box()
        self.chat_player = chat_box()
        self.test_box = input_box()
        # self.rect_chat_recent = input_box(100, 380, 320, 320)
    # recuperation des touche pour le deplacement
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.move_up()

        elif pressed[pygame.K_DOWN]:
            self.player.move_down()

        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()

        elif pressed[pygame.K_LEFT]:
            self.player.move_left()

    def update(self):
        self.map_manager.update()

    # def machin_chouette(self):
    #     self.ancient_message = []
    #     new_message = recent_message.copy()
    #     for message in recent_message:
    #         self.ancient_message.append(pygame.encode_string(message))

    def run(self):

        # gerer les FPS
        clock = pygame.time.Clock()
        
        # boucle du jeu
        running = True

        while running:
            # print(self.ancient_message)

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            self.chat_player.draw_chat(self.screen)
            self.test_box.draw_chat(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                self.chat_player.handle_event(event)
                self.test_box.handle_event(event)
                # self.txt_surface = self.font.render(self.chat_player.recent_message, True, self.chat_player.color)
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    # self.chat_player.text += event.unicode
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_pnj_collision(self.dialog_box)
                        

            clock.tick(60)

        pygame.quit()
