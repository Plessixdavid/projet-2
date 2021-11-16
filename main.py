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
    def my_message(data):
        print('message received with ', data)
        sio.emit('my response', {'response': 'my response'})

    @sio.event
    def disconnect():
        print('disconnected from server')

    sio.connect('http://localhost:6969')
    game.run(sio)
