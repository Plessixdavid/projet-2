# coding : utf-8

import socketio
import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()

    sio = socketio.Client()
    @sio.event
    def connect():
        print('connection established')

    @sio.event
    def disconnect():
        print('disconnected from server')

    sio.connect('http://93.6.41.243:8271/')
    game.run(sio)
