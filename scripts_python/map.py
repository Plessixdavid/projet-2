# coding : utf-8

from dataclasses import dataclass
from menu.main_menu import start as start_menu
import pygame, pytmx, pyscroll
from player import PNJ
from animation import animate_sprite
  

@dataclass
class Portal:
    """nom explicite"""
    from_world: str
    teleport_point: str
    target_world: str
    spawn_point: str


@dataclass
class Map:
    """specifie les donnees que contiennent les maps"""
    name: str
    tmx_data: pytmx.TiledMap
    group: pyscroll.PyscrollGroup
    walls: list[pygame.Rect]
    portals: list[Portal]
    pnjs: list[PNJ]
    lunchs: list[pygame.Rect]
    

class MapManager:
    """
    toutes les donnees et fonctions relative aux maps et a leur affichage
    """

    def __init__(self, screen, player):
        self.maps = dict() # "house" -> Map("house", walls, group, portals)
        self.screen = screen
        self.player = player
        self.current_map = "world"

        # enregistre les maps avec leur specifications propre 
        # ex: si il y a des PNJs
        # la map de depart ...
        self.register_map("world", portals=[
            Portal(from_world="world", teleport_point="enter_inn", target_world="inn", spawn_point="spawn_inn"),
            Portal(from_world="world", teleport_point="enter_my_house", target_world="my_house", spawn_point="spawn_my_house"),
            Portal(from_world="world", teleport_point="teleporter", target_world="new_world", spawn_point="spawn_player")
            ],pnjs=[
            PNJ("paul", nb_points=12, dialog=["Salut ça va ?","Bonne journnée."])
            ,PNJ("hostess", nb_points=1, dialog=["Salut, comment ça va?", "Aurais-tu vue ma licorne?...Non?", "Bonne journnée."])
        ])
        # suivie des autres maps
        self.register_map("my_house", portals=[
            Portal(from_world="my_house", teleport_point="exit_my_house", target_world="world", spawn_point="spawn_my_house_exit")
        ])
        self.register_map("new_world", portals=[
            Portal(from_world="new_world", teleport_point="teleporter", target_world="world", spawn_point="spawn_player")
        ])
        self.register_map("inn", portals=[
            Portal(from_world="inn", teleport_point="exit_inn", target_world="world", spawn_point="spawn_inn_exit")
        ], pnjs=[
            PNJ("hostess", nb_points=1, dialog=[f"Salut, comment ça va ?", "Bienvenue dans la salle d'arcade", "Bonne journnée."])
        ])
        # charge les entites sur les maps
        self.teleport_player("player_start")
        self.teleport_pnjs()

    def check_pnj_collision(self,dialog_box):
        """
        detecte si un PNJ et un joueur son en collision pour permettre ou non l'affichage du dialogue des PNJs
        """
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is PNJ:
                dialog_box.execute(sprite.dialog)
    

    def check_collision(self):
        """
        detecte les collisions et agis en fonctions d'elles
        - teleporte le joueur si il est en contacte avec un portail
        - bloque son deplacement va contre un objet sur lequel on ne peut se deplacer
        - lance le menu des mini-jeux si on entre en contacte avec des objets configurer dans ce but
        """
        for portal in self.get_map().portals: # pour les portail
            if portal.from_world == self.current_map:
                point =self.get_object(portal.teleport_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.spawn_point)

        for sprite in self.get_group().sprites(): # pour les objets sur lesquels on ne peut pas se deplacer
            if type(sprite) is PNJ:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 1
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()
            # pour les objets qui lance le menu des mini-jeux
            if sprite.feet.collidelist(self.get_lunchs()) > -1:
                start_menu()
                sprite.move_back()

    def teleport_player(self, name):
        """
        gere les points de spawn du joueur
        """
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], pnjs=[]):
        """
        charge les donnees du fichier tmx
        et definit des parametres pour chaque maps en fonctions de ces donnees.
        contient (*si present)
        - un zoom
        - une liste d'objets sur lesquels le deplacement est interdit
        - une liste d'objets qui lancent le menu des mini-jeux*
        - des PNJs*
        et enregistre les maps dans un dictionnaire pour resortir les infos au besoins sans recommencer ce processus
        """
        # charger la carte (tmx)
        tmx_data = pytmx.load_pygame(f"ressources/tmx_tsx/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        if name == "world":
            map_layer.zoom = 1.75
            
        if name == "new_world":
            map_layer.zoom = 1.5

        elif name == "my_house":
            map_layer.zoom = 2.4

        elif name == "inn":
            map_layer.zoom = 2.2

        # definir une liste qui va stocker les rectangles de collision
        walls_list = []
        lunchs_list = []
        
        #Boucle qui regarde le type des objets dans le tmx
        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "luncher":
                lunchs_list.append(pygame.Rect( obj.x, obj.y, obj.width, obj.height))
            
                                
        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
        group.add(self.player)

        # recuperer tout les pnjs pour les ajouter au groupe
        for pnj in pnjs:
            group.add(pnj)

        # Enregistrer la nouvelle carte chargée
        self.maps[name] = Map(name, tmx_data, group, walls_list, portals, pnjs, lunchs_list)

    def get_map(self):
        """
        recupere le nom de la map actuelle pour les fonctions
        - 'get_group'
        - 'get_walls'
        - 'get_lunchs'
        - 'get_object'
        """
        return self.maps[self.current_map]

    def get_group(self):
        """
        recupere les groupe d'objets en fonction de la map
        """
        return self.get_map().group

    def get_walls(self):
        """
        recupere les objets sur lesquels le deplacement est interdit en fonction de la map
        """
        return self.get_map().walls

    def get_lunchs(self):
        """
        recupere les objets qui lancent le menu des mini-jeux en fonction de la map
        """
        return self.get_map().lunchs

    def get_object(self, name):
        """
        recupere les objets en fonction de la map
        """ 
        return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_pnjs(self):
        """
        recupere les donnees de chaque map et associe les PNJs ('register_map') avec leur donnees
        pour chaque maps
        """
        for map in self.maps:
            map_data = self.maps[map]
            pnjs = map_data.pnjs

            for pnj in pnjs:
                pnj.load_points(map_data.tmx_data)
                pnj.teleport_spawn()

    # def get_game(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        """
        affiche les donnees trier et assembler par groupe dans la fenetre.
        centre la vue sur le joueur si le zoom et la map actuelle le permet
        """
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        """
        rafraichi en continu les donnees
        """
        self.get_group().update()
        self.check_collision()

        for pnj in self.get_map().pnjs:
            pnj.move()