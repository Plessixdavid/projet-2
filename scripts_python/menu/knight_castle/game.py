import pygame, sys
from menu.knight_castle.setting import *
from menu.knight_castle.level import Level
from menu.knight_castle.overworld import Overworld
from menu.knight_castle.ui import UI
from BDD.DBUtil import DBUtil


class Game3:
    def __init__(self):

        #game attributes
        self.max_level = 0
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0
        self.maxcoins = 0

        # Audio
        self.level_bg_music = pygame.mixer.Sound('scripts_python/menu/knight_castle/audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('scripts_python/menu/knight_castle/audio/overworld_music.wav')

        # Overworld création
        self.overworld = Overworld(0,self.max_level,screen,self.create_level)
        self.status ='overworld'
        

        # User interface
        self.ui = UI(screen)

    def create_level(self,current_level):
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
        self.status = 'level'
        
        self.level_bg_music.play(loops = -1)

    def create_overworld(self,current_level,new_max_level):
        if new_max_level> self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops = -1)
        self.level_bg_music.stop()


    def change_coins(self,amount):
        self.coins += amount

    def change_health(self,amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.maxcoins = self.coins
            Query = "INSERT INTO knight_castle (score, nameid ) VALUES (%s, %s)"
            Values = (self.maxcoins, 1)
            DBUtil.ExecuteQuery(Query, Values)
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0,self.max_level,screen,self.create_level)
            self.status ='overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops = -1)

    def run(self):
        if self.status == 'overworld':

            pygame.display.flip()
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()

    def startGame(self):
        self.running = True   
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                

            # screen.fill('grey')
            self.run()
            pygame.display.update()
            clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game3()
    


