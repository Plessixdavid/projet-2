# coding : utf-8

import pygame
import socketio
from map import MapManager
from entity import Player
from animation import animate_sprite
from dialog import dialog_box
from player_chat import chat_box

class Game:

    def __init__(self, pseudo):
        # créer la fenetre du jeu
        infoObject = pygame.display.Info()
        self.DISPLAY_W, self.DISPLAY_H =  infoObject.current_w, infoObject.current_h
        self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("hub")

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        #genere un boite de dialogue
        self.dialog_box = dialog_box()
        self.chat_player = None
        self.player_name = pseudo

    # recuperation des touche pour le deplacement
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]: # pour vers le haut
            self.player.move_up()
            self.player.change_animation("up")

        elif pressed[pygame.K_DOWN]: # pour vers le bas
            self.player.move_down()
            self.player.change_animation("down")

        elif pressed[pygame.K_RIGHT]: # pour vers la droite
            self.player.move_right()
            self.player.change_animation("right")

        elif pressed[pygame.K_LEFT]: # pour vers la gauche
            self.player.move_left()
            self.player.change_animation("left")
        
        


    def update(self): # pour rafraichire l'affichage de la map
        self.map_manager.update()
    

    def run(self):
        # Creating Socket
        sio = socketio.Client()

        # This event is triggered when the socket connects for the first time
        @sio.event
        def connect():
            print('connection established')
            sio.emit("JOIN", {
            'pos': self.player.position,
            'map': "world"
            })

        connected = False

        # Try to connect to the server, if this fail the game will just run on solo
        try:
            sio.connect('http://109.11.96.12:8271/') # Public server
            # sio.connect('http://localhost:6969/') # Local server
            self.chat_player = chat_box(sio=sio, pseudo=self.player_name)
            connected = True
        except: 
            self.chat_player = chat_box(pseudo=self.player_name)
            pass

        # gerer les FPS
        clock = pygame.time.Clock()
        
        # boucle du jeu
        running = True

        # Guest list
        players = []

        # The server send every players data, we add it to the guest list
        @sio.on("GET")
        def addPlayers(data):
            players.clear()
            players.extend(data)

        while running:
            self.player.save_location()
            self.handle_input()
            self.update()

            if connected == True:
                # Retrieve list of every player
                sio.emit("GET")

                # Update our position in the server ONLY if we move
                if self.player.old_position != self.player.position:
                    sio.emit("UPDATE POS", {
                        'pos': self.player.position,
                        'map': self.map_manager.current_map
                    })

                # Print every players to the map except us
                for player in players:
                    if player['id'] == sio.get_sid() or player['map'] != self.map_manager.current_map:
                        continue

                    # Create the guest
                    guest = Player("player", player['pos'][0],player['pos'][1])
                    guest.update()

                    # Add the guest to the group at layer 99
                    self.map_manager.get_group().add(guest, layer=99)

            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            self.chat_player.draw_chat(self.screen)
            
            # animate_sprite.get_name(self.screen)
            pygame.display.flip()

            for event in pygame.event.get(): # recuperation des events
                self.chat_player.handle_event(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_pnj_collision(self.dialog_box)
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()

            # Remove every element at layer 99 (all our guests)
            self.map_manager.get_group().remove_sprites_of_layer(99)

            clock.tick(60)

        if connected == True:
            # Disconnect the socket
            sio.disconnect()
        pygame.quit()
