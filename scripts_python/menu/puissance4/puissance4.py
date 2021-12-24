import numpy as np

NBligne= 6
NBcolon= 7

def createboard():
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
    for row in range(NBligne):
        if plateau[row][colonne] == 0:
            return row


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
    for colon in range (NBcolon-3):
        for row in range (NBligne):
            if plateau[row][colon]== jeton and plateau[row][colon+1]== jeton and plateau[row][colon+2]== jeton and plateau[row][colon+3]== jeton:
                return True

    #test de toutes les positions verticales
    for colon in range (NBcolon):
        for row in range (NBligne-3):
            if plateau[row][colon]== jeton and plateau[row+1][colon]== jeton and plateau[row+2][colon]== jeton and plateau[row+3][colon]== jeton:
                return True

    #test de toutes les positions diagonales orientées vers la droite
    for colon in range (NBcolon-3):
        for row in range (NBligne-3):
            if plateau[row][colon]== jeton and plateau[row+1][colon+1]== jeton and plateau[row+2][colon+2]== jeton and plateau[row+3][colon+3]== jeton:
                return True

    #test de toutes les positions diagonales orientées vers la gauche
    for colon in range (NBcolon-3):
        for row in range (3,NBligne):
            if plateau[row][colon]== jeton and plateau[row-1][colon+1]== jeton and plateau[row-2][colon+2]== jeton and plateau[row-3][colon+3]== jeton:
                return True


def Partienulle(plateau):
    for colon in range (NBcolon):
        for row in range(NBligne):
            if plateau[row][colon] == 0:
                return False
    return True
