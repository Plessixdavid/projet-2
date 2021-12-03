# coding : utf-8

from dataclasses import dataclass
import pygame, pytmx, pyscroll

@dataclass
class Portal:
    from_world: str
    teleport_point: str
    target_world: str
    spawn_point: str

@dataclass
class Map:
    name: str
    tmx_data: pytmx.TiledMap
    group: pyscroll.PyscrollGroup
    walls: list[pygame.Rect]
    portals: list[Portal]

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict() # "house" -> Map("house", walls, group, portals)
        self.screen = screen
        self.player = player
        self.current_map = "world"

        self.register_map("world", portals=[
            Portal(from_world="world", teleport_point="enter_inn", target_world="inn", spawn_point="spawn_inn"),
            Portal(from_world="world", teleport_point="enter_my_house", target_world="my_house", spawn_point="spawn_my_house"),
            Portal(from_world="world", teleport_point="teleporter", target_world="new_world", spawn_point="spawn_player")
        ])
        self.register_map("my_house", portals=[
            Portal(from_world="my_house", teleport_point="exit_my_house", target_world="world", spawn_point="spawn_my_house_exit")
        ])
        self.register_map("new_world", portals=[
            Portal(from_world="new_world", teleport_point="teleporter", target_world="world", spawn_point="spawn_player")
        ])
        self.register_map("inn", portals=[
            Portal(from_world="inn", teleport_point="exit_inn", target_world="world", spawn_point="spawn_inn_exit")
        ])

        self.teleport_player("player_start")

    def check_collision(self):
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point =self.get_object(portal.teleport_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.spawn_point)

        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[]):
        # charger la carte (tmx)
        tmx_data = pytmx.load_pygame(f"ressources/tmx_tsx/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.75

        # definir une liste qui va stocker les rectangles de collision
        walls_list = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        group.add(self.player)

        # Enregistrer la nouvelle carte chargée
        self.maps[name] = Map(name, tmx_data, group, walls=walls_list, portals=portals)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collision()