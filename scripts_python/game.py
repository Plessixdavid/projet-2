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
            connected = True
        except: 
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
                    guest = Player(player['pos'][0],player['pos'][1])
                    guest.update()

                    # Add the guest to the group at layer 99
                    self.map_manager.get_group().add(guest, layer=99)

            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Remove every element at layer 99 (all our guests)
            self.map_manager.get_group().remove_sprites_of_layer(99)

            clock.tick(60)

        if connected == True:
            # Disconnect the socket
            sio.disconnect()
        pygame.quit()
