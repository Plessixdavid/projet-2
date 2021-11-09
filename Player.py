# coding: utf-8
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.Health = 100
        self.Max_Health = 100
        self.Attack = 10
        self.Velocity = 10
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def Move_Right(self):
        self.rect.x += self.Velocity

    def Move_Left(self):
        self.rect.x -= self.Velocity

    def Move_up(self):
        self.rect.y -= self.Velocity

    def Move_Down(self):
        self.rect.y += self.Velocity
