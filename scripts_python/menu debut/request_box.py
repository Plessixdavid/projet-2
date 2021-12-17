# import sys module
import pygame
import sys
  
  
# pygame.init() will initialize all
# imported module
pygame.init()
  
clock = pygame.time.Clock()
  
# it will display on screen
screen = pygame.display.set_mode([600, 500])
  
# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_pseudo = ''
user_mdp = ''
  
# create rectangle
input_pseudo = pygame.Rect(200, 200, 140, 32)
input_mdp = pygame.Rect(100, 100, 140, 32)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')

pseudo_color = color_passive
mdp_color = color_passive
  
pseudo_active = False
mdp_active = False

while True:
    for event in pygame.event.get():
  
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_pseudo.collidepoint(event.pos):
                pseudo_active = True
                mdp_active = False
            elif input_mdp.collidepoint(event.pos):
                mdp_active = True
                pseudo_active = False
            else:
                mdp_active = False
                pseudo_active = False
            
  
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                if pseudo_active:
                    # get text input from 0 to -1 i.e. end.
                    user_pseudo = user_pseudo[:-1]
                if mdp_active:
                    user_mdp = user_mdp[:-1]
            else:
                if pseudo_active:
                    user_pseudo += event.unicode
                if mdp_active:
                    user_mdp += event.unicode
    # it will set background color of screen
    screen.fill((255, 255, 255))
  
    pseudo_color = color_active if pseudo_active else color_passive
    mdp_color = color_active if mdp_active else color_passive
          
    # draw pseudoangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, pseudo_color, input_pseudo)
    pygame.draw.rect(screen, mdp_color, input_mdp)
  
    pseudo_surface = base_font.render(user_pseudo, True, (255, 255, 255))
    mdp_surface2 = base_font.render(user_mdp, True, (255, 255, 255))

    # render at position stated in arguments
    screen.blit(pseudo_surface, (input_pseudo.x+5, input_pseudo.y+5))
    screen.blit(mdp_surface2, (input_mdp.x+5, input_mdp.y+5))
    
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_pseudo.w = max(100, pseudo_surface.get_width()+10)
    input_mdp.w = max(100, mdp_surface2.get_width()+10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)