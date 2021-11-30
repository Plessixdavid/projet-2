import pygame , sys
from settings import *
from player_class import*


pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.Clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30
        self.player = Player(self, PLAYER_START_POS)

        self.load()

    def run(self):
        while self.running:
            if self.state == 'start' :
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing' :
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.Clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

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
        self.background = pygame.image.load('PacMan/maze.png')
        self.background = pygame.transform.scale(self.background,(MAZE_WIDTH,MAZE_HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0),(x*self.cell_width,HEIGHT))
        for y in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0,y*self.cell_height),(WIDTH,y*self.cell_height))

############################## intro Functions #######################

    def start_events(self):
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                self.state = 'playing'

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

    def playing_update(self):
        self.player.update()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        self.draw_grid()
        self.draw_text('CURRENT SCORE: 0', self.screen, (60,0), 18, YELLOW1, 'Arial Black', centered = False)
        self.draw_text('HIGH SCORE: 0', self.screen, (WIDTH//2 + 60,0), 18, YELLOW1, 'Arial Black', centered = False)
        self.player.draw()
        pygame.display.update()
