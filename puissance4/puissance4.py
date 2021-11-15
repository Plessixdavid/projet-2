import numpy as np

NBligne= 6
NBcolon= 7


def createboard ():
    """
        créer une matrice NB_LIGNE, NB_COLONNE remplie de zeros
    """
    Plateau = np.zeros ((NBligne,NBcolon))
    return Plateau



def afficherPlateau(Plateau):
    """
        afficher la matrice en inversant l'ordre des lignes :
    """
    print(np.flip(Plateau,0))



def validemplacement(Plateau,colonne):
    """
        Y a t'il encore de la place dans la colonne choisie
    """
    if Plateau[NBligne-1][colonne] == 0 :
        return True
    else:
        return False


def trouver_Ligne_Vide(plateau,colonne):
    """
        quelle est la ligne libre dans la colonne choisie    
    """
    for r in range(NBligne):
        if plateau[r][colonne]==0:
            return r


def LacherJeton(plateau, ligne, colonne, jeton) :
    """
        placer le numéro du joueur dans la colonne choisie, sur la ligne libre
    """
    plateau[ligne][colonne] = jeton
    

def coup_gagnant(plateau, jeton):
    """
        #On teste dans toutes les directions, s'il y a 4 jetons identiques qui se suivent
    """
    
    #test de toutes les positions horizontales
    for c in range (NBcolon-3):
        for r in range (NBligne):
            if plateau[r][c]== jeton and plateau[r][c+1]== jeton and plateau[r][c+2]== jeton and plateau[r][c+3]== jeton:
                return True

    #test de toutes les positions verticales
    for c in range (NBcolon):
        for r in range (NBligne-3):
            if plateau[r][c]== jeton and plateau[r+1][c]== jeton and plateau[r+2][c]== jeton and plateau[r+3][c]== jeton:
                return True

    #test de toutes les positions diagonales orientées vers la droite
    for c in range (NBcolon-3):
        for r in range (NBligne-3):
            if plateau[r][c]== jeton and plateau[r+1][c+1]== jeton and plateau[r+2][c+2]== jeton and plateau[r+3][c+3]== jeton:
                return True

    #test de toutes les positions diagonales orientées vers la gauche
    for c in range (NBcolon-3):
        for r in range (3,NBligne):
            if plateau[r][c]== jeton and plateau[r-1][c+1]== jeton and plateau[r-2][c+2]== jeton and plateau[r-3][c+3]== jeton:
                return True
   

