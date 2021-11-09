# coding: utf-8
import sys,pygame

class Player:
    list = []
    def __init__(self, screen, size: int = 20, color: tuple = (255, 0, 0), x: int = 20, y:int = 20) -> None:
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        self.size = size
        self.rect = pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), size)

        self.list.append(self)


    def draw(self, screen: pygame.Surface) -> None:
        self.rect = pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)

    def collision(self, size, next_y:int = None, next_x:int = None) -> bool:
        next_y = next_y if next_y is not None else self.pos_y
        next_x = next_x if next_x is not None else self.pos_x

        width, height = size


        if next_x-20 < 0 or next_x+20 > width:
            return True
        if next_y-20 < 0 or next_y+20 > height:
            return True

        for player in Player.list:
            if player == self: continue
            print(player.rect.right, self.rect.left)
            if player.rect.right < self.rect.left:
                return False

            if player.rect.bottom < self.rect.top:
                return False

            if player.rect.left > self.rect.right:
                return False

            if player.rect.top > self.rect.bottom:
                return False

            return True

        return False
        

    def isMoving(self) -> None:
        if not self.move_left and not self.move_right and not self.move_up and not self.move_down:
            return

        size = (700,700)
        if self.move_left:
            if self.collision(size, next_x=self.pos_x - 1, next_rect=pygame.Rect(self.rect.left, self.rect.top)): return
            self.pos_x -= 1
        
        if self.move_right:
            if self.collision(size, next_x=self.pos_x + 1): return
            self.pos_x += 1

        if self.move_up:
            if self.collision(size, next_y=self.pos_y - 1): return
            self.pos_y -= 1

        if self.move_down:
            if self.collision(size, next_y=self.pos_y + 1): return
            self.pos_y += 1

    @classmethod
    def drawPlayers(cls, screen):
        for player in cls.list:
            player.draw(screen)

    @classmethod
    def movePlayers(cls):
        for player in cls.list:
            player.isMoving()

def main() :
    pygame.init()

    RUNNING = True

    size = width, height = 700, 700

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TUFF")

    myPlayer = Player(screen)
    secondPlayer = Player(screen, 40, (0,0,255), x= 270, y=270)

    print(myPlayer.rect)

    while RUNNING:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                RUNNING = False

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        myPlayer.move_left = True
                    case pygame.K_RIGHT:
                        myPlayer.move_right = True
                    case pygame.K_UP:
                        myPlayer.move_up = True  
                    case pygame.K_DOWN:
                        myPlayer.move_down = True
                    case pygame.K_LSHIFT:
                        myPlayer.pos_x += 100
                    case pygame.K_z:
                        secondPlayer.move_up = True
                    case pygame.K_s:
                        secondPlayer.move_down = True
                    case pygame.K_q:
                        secondPlayer.move_left = True
                    case pygame.K_d:
                        secondPlayer.move_right = True


            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT:
                        myPlayer.move_left = False
                    case pygame.K_RIGHT:
                        myPlayer.move_right = False
                    case pygame.K_UP:
                        myPlayer.move_up = False  
                    case pygame.K_DOWN:
                        myPlayer.move_down = False
                    case pygame.K_z:
                        secondPlayer.move_up = False
                    case pygame.K_s:
                        secondPlayer.move_down = False
                    case pygame.K_q:
                        secondPlayer.move_left = False
                    case pygame.K_d:
                        secondPlayer.move_right = False


                    
                






        Player.movePlayers()

        screen.fill((  0, 0,   0))
        Player.drawPlayers(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()
