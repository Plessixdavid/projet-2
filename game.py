# coding : utf-8

import pygame
import pytmx
import pyscroll

from player import Player

class Game:

    def __init__(self):
        # créer la fenetre du jeu
        self.screen = pygame.display.set_mode((800,700))
        pygame.display.set_caption("PYGAMON")

        # charger la carte (tmx)
        tmx_data = pytmx.load_pygame("ressources/fichiers_tmx/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y)

        # definir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        self.group.add(self.player)

        # definir le rect de collision pour entrer dans la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    # recuperation des touche pour le deplacement
    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")

        if pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")

        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")

        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")

    def switch_house(self):
        # charger la carte (tmx)
        tmx_data = pytmx.load_pygame("ressources/fichiers_tmx/my_house.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # definir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        self.group.add(self.player)

        # definir le rect de collision pour entrer dans la maison
        enter_house = tmx_data.get_object_by_name("exit_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # recuperer le point de spawn dans la maison
        spawn_house_point = tmx_data.get_object_by_name("spawn_house")
        self.player.position[0] = spawn_house_point.x - 16
        self.player.position[1] = spawn_house_point.y - 32
            
    def switch_world(self):
        # charger la carte (tmx)
        tmx_data = pytmx.load_pygame("ressources/fichiers_tmx/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # definir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        self.group.add(self.player)

        # definir le rect de collision pour entrer dans la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # recuperer le point de spawn devant la maison
        spawn_house_point = tmx_data.get_object_by_name("spawn_house_exit")
        self.player.position[0] = spawn_house_point.x - 16
        self.player.position[1] = spawn_house_point.y

    def update(self):
        self.group.update()
        self.map = "world"

        # verifier l'entrer dans la maison
        if self.map == "world" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()
            self.map = "house"

        # verifier la sortie de la maison
        if self.map == "house" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_world()
            self.map = "world"

        # verification des collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                self.player.move_back()

    def run(self, sio):

        sio.emit("JOIN", {
            'pos': self.player.position,
            'map': "world"
            })
        # gerer les FPS
        clock = pygame.time.Clock()
        
        # boucle du jeu
        running = True

        my_sid = sio.get_sid()

        players = []

        @sio.on("GET")
        def test(data):
            players.clear()
            players.extend(data)

        while running:
            sio.emit("GET")

            self.player.save_location()
            self.handle_input()
            
            if (self.player.old_position != self.player.position):
                sio.emit("UPDATE POS", {
                    'pos': self.player.position,
                    'map': self.map
                })

            self.update()
            self.group.center(self.player.rect.center)

            for player in players:
                if player['id'] == my_sid or player['map'] != self.map:
                    continue

                self.group.add(Player(player['pos'][0],player['pos'][1]).update(), layer=99)

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sio.disconnect()
                    running = False

            self.group.remove_sprites_of_layer(99)

            clock.tick(60)

        pygame.quit()
