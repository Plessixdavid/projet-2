# coding : utf-8

import pygame
from animation import animate_sprite

class Entity (animate_sprite):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def save_location(self):
        self.old_position = self.position.copy()

    def move_up(self): 
        pressed = pygame.key.get_pressed()
        self.change_animation("up")
        if pressed[pygame.K_SPACE]:
            self.position[1] -= self.speed*1.5
            self.speed_clock = 130
        else:
            self.position[1] -= self.speed
            self.speed_clock = 180

    def move_down(self): 
        pressed = pygame.key.get_pressed()
        self.change_animation("down")
        if pressed[pygame.K_SPACE]:
            self.position[1] += self.speed*1.5
            self.speed_clock = 130
        else:
            self.position[1] += self.speed
            self.speed_clock = 180

    def move_right(self): 
        pressed = pygame.key.get_pressed()
        self.change_animation("right")
        if pressed[pygame.K_SPACE]:
            self.position[0] += self.speed*1.5
            self.speed_clock = 130
        else:
            self.position[0] += self.speed
            self.speed_clock = 180

    def move_left(self): 
        pressed = pygame.key.get_pressed()
        self.change_animation("left")
        if pressed[pygame.K_SPACE]:
            self.position[0] -= self.speed*1.5
            self.speed_clock = 130
        else:
            self.position[0] -= self.speed
            self.speed_clock = 180
        
    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

class Player(Entity):

    def __init__(self):
        super().__init__("player", 0, 0)
        self.image = self.get_image(32, 0)
        self.image.set_colorkey([0, 0, 0])

class PNJ(Entity):

    def __init__(self, name, nb_points, dialog):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.speed = 1.15
        self.current_point = 0

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points: target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]
        
        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3: self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3: self.move_up()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3: self.move_right()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3: self.move_left()

        if self.rect.colliderect(target_rect): self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path_{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)