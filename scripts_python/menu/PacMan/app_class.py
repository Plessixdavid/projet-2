import pygame , sys, copy
from menu.PacMan.settings import *
from menu.PacMan.player_class import*
from menu.PacMan.enemy_class import *
from BDD.DBUtil import DBUtil



pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.Clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.player = Player(self, vec(self.p_pos)) 
        self.make_enemies ()
        self.High_Score = 0
    
    def run(self):
        self.m = True
        self.m2 = True
        while self.running:
            if self.state == 'start' :
                self.start_events()
                self.start_update()
                self.start_draw()
            
            elif self.state == 'playing' :
                self.playing_events()
                self.playing_update()
                self.playing_draw()

            elif self.state == 'game over' :
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()

            else:
                self.running = False
            self.Clock.tick(FPS)
            

############################## Helper Functions #######################        
    def draw_text(self, words, screen , pos, size, colour ,font_name, centered = False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered :
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)
            
    def load(self):
        self.background = pygame.image.load('scripts_python/menu/PacMan/maze.png')
        self.background = pygame.transform.scale(self.background,(MAZE_WIDTH,MAZE_HEIGHT))
        
        # Opening walls file
        # creating walls list with coords of walls
        # stored as a vector
        with open("scripts_python/menu/PacMan/walls.txt",'r') as file :
            for yidx,line in enumerate(file) :
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["1","2","3","4","5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char  == "B" :
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height, self.cell_width, self.cell_height))
                    

    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0),(x*self.cell_width,HEIGHT))
        for y in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0,y*self.cell_height),(WIDTH,y*self.cell_height))
        # for coins in self.coins:
        #     pygame.draw.rect(self.background,(167, 179, 34),(coins.x*self.cell_width, coins.y*self.cell_height, self.cell_width, self.cell_height))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec (enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0

        self.coins = []
        with open("PacMan/walls.txt",'r') as file :
            for yidx,line in enumerate(file) :
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
        self.state = "playing"
############################## intro Functions #######################

    
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                self.state = 'playing'
            if self.m == True : 
                pygame.mixer.music.load("scripts_python/menu/PacMan/song/intro.wav")
                pygame.mixer.music.play(1)
                self.m=False


    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR',self.screen, [WIDTH//2,HEIGHT//2], START_TEXT_SIZE , (255, 9, 33), START_FONT, centered = True)
        self.draw_text('PLAYER 1',self.screen, [WIDTH//2,HEIGHT//2 +75], START_TEXT_SIZE , (121, 28, 248), START_FONT, centered = True)
        self.draw_text('High Score',self.screen, [4,0], START_TEXT_SIZE , (44, 117, 255), START_FONT)
        pygame.display.update()

############################## playing Functions #######################

    def playing_events(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
                if event.key == pygame.K_DOWN :
                    self.player.move(vec(0,1))
                if self.m2 == False : 
                    pygame.mixer.music.load("scripts_python/menu/PacMan/song/animaux.mp3")
                    pygame.mixer.music.play(10)
                    self.m2=False

    def playing_update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies :
            if enemy.grid_pos == self.player.grid_pos :
                self.remove_life()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        self.draw_coins()
        # self.draw_grid()
        self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score), self.screen, (60,0), 18, YELLOW1, 'Arial Black', centered = False)
        self.draw_text('HIGH SCORE: {}'.format(self.High_Score), self.screen, (WIDTH//2 + 60,0), 18, YELLOW1, 'Arial Black', centered = False)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update()
        
    def remove_life(self):
        self.player.lives -= 1
        pygame.mixer.music.load("scripts_python/menu/PacMan/song/death.wav")
        pygame.mixer.music.play(1)
        self.m2 = True
        if self.player.lives == 0 :
            if self.player.current_score > self.High_Score :
                self.High_Score = self.player.current_score
                Query = "INSERT INTO pac_man (score, nameid ) VALUES (%s, %s)"
                Values = (self.High_Score, 1)
                DBUtil.ExecuteQuery(Query, Values)
            self.state = "game over"
        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies :
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0
            

    def draw_coins(self):
        for coin in self.coins :
            pygame.draw.circle(self.screen, (124, 123, 7),(int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2,
            int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2),5)


############################## GAME OVER Functions #######################

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                self.running = False

    def game_over_update(self):
        pass

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press the escape button to QUIT"
        again_text = "Pres the SPACE bar to PLAY AGAIN"
        self.draw_text ("GAME OVER", self.screen, [WIDTH//2, 100], 52, RED, START_FONT, centered = True)
        self.draw_text (quit_text, self.screen, [WIDTH//2, HEIGHT//2], 36, BLUE, START_FONT, centered = True)
        self.draw_text (again_text, self.screen, [WIDTH//2, HEIGHT//1.5], 36, BLUE, START_FONT, centered = True)

        pygame.display.update()