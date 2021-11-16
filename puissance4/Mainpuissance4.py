import puissance4


plateau = puissance4.createboard()
game_over = False
tour = 0
puissance4.afficherPlateau(plateau)

while not game_over:
 
 #joueur 1
    
 #choix du numéro de colonne par le joueur 1
    correct = False
    
    while not correct:
        colonne = int(input("Joueur 1 : Entrez la colonne sélectionnée (0-6):"))-1
        
        if colonne >= 0 and colonne <= 6 :
            correct = True
    
    if puissance4.validemplacement(plateau,colonne):
    
    #trouver la ligne libre dans la colonne choisie
        ligne = puissance4.trouver_Ligne_Vide(plateau,colonne)
    #mettre dans la matrice la valeur 1 dans la ligne, colonne
        puissance4.LacherJeton(plateau, ligne, colonne,jeton = 1)
    #tester si le joueur 1 a gagné
        if puissance4.coup_gagnant(plateau,1):
            print("Le joueur 1 a gagné!!! Bravo")
            game_over = True
    tour += 1

    puissance4.afficherPlateau(plateau)

    #joueur 2

#choix du numéro de colonne par le joueur 23
    correct = False
    
    while not correct:
        colonne = int(input("Joueur 2 : Entrez la colonne sélectionnée (0-6):"))-1
        
        if colonne >= 0 and colonne <= 6 :
            correct = True
    
    if puissance4.validemplacement(plateau,colonne):
    
    #trouver la ligne libre dans la colonne choisie
        ligne = puissance4.trouver_Ligne_Vide(plateau,colonne)
    #mettre dans la matrice la valeur 1 dans la ligne, colonne
        puissance4.LacherJeton(plateau, ligne, colonne,2)
    #tester si le joueur 1 a gagné
        if puissance4.coup_gagnant(plateau,2):
            print("Le joueur 2 a gagné!!! Bravo")
            game_over = True

    puissance4.afficherPlateau(plateau)
    if puissance4.Partienulle(plateau):
        print("Partie nulle")
        game_over = True
