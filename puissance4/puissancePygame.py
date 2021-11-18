import pygame
from pygame.constants import MOUSEBUTTONDOWN
import puissance4
import math

#Les constantes
LARGEUR_CASE = 100
BLEU = (0,0,255)
ROUGE = (255,0,0)
JAUNE = (255,255,0)
NOIR = (0,0,0)
BLANC = (255,255,255)
RAYON= int(LARGEUR_CASE/2)-4

def Dessinerplateau(plateau):
    """
    """
            #draw plateau 
    pygame.draw.rect(ecran,BLEU,(0,LARGEUR_CASE,puissance4.NBcolon * LARGEUR_CASE,(puissance4.NBligne+1) * LARGEUR_CASE))  
    for colon in range (puissance4.NBcolon):
        
        for row in range(puissance4.NBligne):
            pygame.draw.circle(ecran,NOIR,(int(colon*LARGEUR_CASE+LARGEUR_CASE/2),int(row*LARGEUR_CASE+LARGEUR_CASE/2+LARGEUR_CASE)),RAYON)
            pygame.display.update()

    # draw jeton
    for colon in range (puissance4.NBcolon):
       
        for row in range (puissance4.NBligne):
            
            if plateau[row][colon] == 1 :
                pygame.draw.circle(ecran,ROUGE,(int(colon*LARGEUR_CASE+LARGEUR_CASE/2),
                hauteur- int(row*LARGEUR_CASE+LARGEUR_CASE/2)),RAYON)
            
            if plateau[row][colon] == 2 :
                pygame.draw.circle(ecran,JAUNE,(int(colon*LARGEUR_CASE+LARGEUR_CASE/2),
                hauteur- int(row*LARGEUR_CASE+LARGEUR_CASE/2)),RAYON)
            
            pygame.display.update()



pygame.init()
largeur = puissance4.NBcolon * LARGEUR_CASE
hauteur = (puissance4.NBligne+1) * LARGEUR_CASE
ecran = pygame.display.set_mode((largeur, hauteur))
plateau = puissance4.createboard()
Dessinerplateau(plateau)    
game_over = False
tour = 0
myfont = pygame.font.SysFont("comicsansms", 40)
while not game_over :
    
    for event in pygame.event.get():
        
        #on déplace le jeton avec la souris
        if event.type == pygame.MOUSEMOTION:
            #effacer la première ligne du plateau
            pygame.draw.rect(ecran,NOIR,(0,0,largeur,LARGEUR_CASE))
            #position de la souris
            posx = event.pos[0]
            #si joueur 1 on affiche un jeton rouge, à la position x de la souris
            if tour==0:
                pygame.draw.circle(ecran,ROUGE,(posx,int(LARGEUR_CASE/2)),RAYON)
                #si joueur 2 on affiche un jeton jaune, à la position x de la souris
            else:
                pygame.draw.circle(ecran,JAUNE,(posx,int(LARGEUR_CASE/2)),RAYON)
                #on met l'écran à jour
            pygame.display.update()

        if event.type==pygame.QUIT:
            game_over = True
            pygame.quit() 

# player 1 choice of position jeton
        if event.type == pygame.MOUSEBUTTONDOWN :
            #effacer la première ligne du plateau 
            if tour == 0 :
                posx = event.pos[0] # position du de la souris au moment du click
                colonne = int(math.floor(posx/LARGEUR_CASE))
                
                if puissance4.validemplacement(plateau,colonne):
                    #trouver la ligne libre dans la colonne choisie
                    ligne = puissance4.trouver_Ligne_Vide(plateau,colonne)
                    #mettre dans la matrice la valeur 1 dans la ligne, colonne
                    puissance4.LacherJeton(plateau, ligne, colonne,1)
                    #tester si le joueur 1 a gagné
                    if puissance4.coup_gagnant(plateau,1):
                        pygame.draw.circle(ecran, ROUGE, (int(LARGEUR_CASE/2), int(LARGEUR_CASE/2)),RAYON)
                        texte_image = myfont.render("Le joueur 1 a gagné", True, ROUGE)
                        ecran.blit(texte_image, [50, 10])
                        game_over = True
                tour = 1
                Dessinerplateau(plateau)


            # player 2 choice of position jeton
            else :
                #effacer la première ligne du plateau
                pygame.draw.rect(ecran,NOIR,(0,0,largeur,LARGEUR_CASE))
                posx = event.pos[0] # position du de la souris au moment du click
                colonne = int(math.floor(posx/LARGEUR_CASE))
                if puissance4.validemplacement(plateau,colonne):
                    #trouver la ligne libre dans la colonne choisie
                    ligne = puissance4.trouver_Ligne_Vide(plateau,colonne)
                    #mettre dans la matrice la valeur 2 dans la ligne, colonne
                    puissance4.LacherJeton(plateau, ligne, colonne,2)
                    #tester si le joueur 2 a gagné
                    if puissance4.coup_gagnant(plateau,2):
                        pygame.draw.circle(ecran, JAUNE, (int(LARGEUR_CASE/2), int(LARGEUR_CASE/2)),RAYON)
                        texte_image = myfont.render("Le joueur 2 a gagné", True, JAUNE)
                        ecran.blit(texte_image, [50, 10])
                        game_over = True
                tour=0
                #afficher le jeton du joueur 1
                Dessinerplateau(plateau) 
    if puissance4.Partienulle(plateau):
        texte_image = myfont.render("Match nul ", True, BLANC)
        ecran.blit(texte_image, [50, 10])
        game_over = True
pygame.time.wait(3000)
pygame.quit()
    




