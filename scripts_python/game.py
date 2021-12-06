# coding : utf-8

import pygame
import socketio
from map import MapManager
from player import Player

class Game:

    def __init__(self):
        # créer la fenetre du jeu
        self.screen = pygame.display.set_mode((900,780))
        pygame.display.set_caption("PYGAMON")

        # generer un joueur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    # recuperation des touche pour le deplacement
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")

        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")

        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")

        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")

    def update(self):
        self.map_manager.update()

    def run(self):

        sio = socketio.Client()
        @sio.event
        def connect():
            print('connection established')
            sio.emit("JOIN", {
            'pos': self.player.position,
            'map': "world"
            })

        @sio.event
        def disconnect():
            print('disconnected from server')

        try:
            # sio.connect('http://93.6.41.243:8271/')
            sio.connect('http://localhost:6969/')
        except: 
            pass

        # gerer les FPS
        clock = pygame.time.Clock()
        
        # boucle du jeu
        running = True

        players = []

        @sio.on("GET")
        def addPlayers(data):
            players.clear()
            players.extend(data)

        while running:
            sio.emit("GET")

            self.player.save_location()
            self.handle_input()
            self.update()
            

            if (self.player.old_position != self.player.position):
                print(self.map_manager.current_map)
                sio.emit("UPDATE POS", {
                    'pos': self.player.position,
                    'map': self.map_manager.current_map
                })


            for player in players:
                if player['id'] == sio.get_sid():
                    continue
                
                # print(player['map'])
                if player['map'] != self.map_manager.current_map:
                    continue

                mul_player = Player(player['pos'][0],player['pos'][1])
                mul_player.update()

                self.map_manager.get_group().add(mul_player, layer=99)

            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.map_manager.get_group().remove_sprites_of_layer(99)
            clock.tick(60)

        sio.disconnect()
        pygame.quit()
