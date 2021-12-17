# coding: utf-8

# imports
from DBUtil import DBUtil
from Data_joueur import Data_joueur
from Pac_man import Pac_man
from Score_jeux2 import Score_jeux2
from Score_jeux3 import Score_jeux3
from Score_jeux4 import Score_jeux4
from Score_jeux5 import Score_jeux5
from Score_jeux6 import Score_jeux6
from Skin import Skin


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("Projet coconuts")
    
    # get categories
    DBUtil.FillModelCollection("SELECT * FROM Skin", Skin)
    DBUtil.FillModelCollection("SELECT * FROM Data_joueur", Data_joueur)
    DBUtil.FillModelCollection("SELECT * FROM Pac_man", Pac_man)
    DBUtil.FillModelCollection("SELECT * FROM Score_jeux2", Score_jeux2)
    DBUtil.FillModelCollection("SELECT * FROM Score_jeux3", Score_jeux3)
    DBUtil.FillModelCollection("SELECT * FROM Score_jeux4", Score_jeux4)
    DBUtil.FillModelCollection("SELECT * FROM Score_jeux5", Score_jeux5)
    DBUtil.FillModelCollection("SELECT * FROM Score_jeux6", Score_jeux6)
    
    # name = input("saisissez nom ")
    # Motdp = input("saisissez mot de passe ")
    # Mail = input("saisissez email ")
    # image = int(input("saisissez un numero de skin \n lapin(1)\n licorne(2)\n tortue(3)\n"))
    
    # # INSERT DATA
    # Query = "INSERT INTO data_joueur (mot_de_passe, email, skinid, Name ) VALUES (%s, %s, %s, %s)"
    # Values = (Motdp, Mail, image, name)
    # DBUtil.ExecuteQuery(Query, Values)
    # DBUtil.Close()
    
    # input("Suite DELETE ...")
    # Query = "DELETE FROM data_joueur WHERE id = %s"
    # Values = (13,)
    # DBUtil.ExecuteQuery(Query, Values)
    # DBUtil.Close()
   
    
    
    
    # close DB
    DBUtil.Close()
  
    # print model content
    PrintCollection(Data_joueur)
    PrintCollection(Pac_man)
    # PrintCollection(Score_jeux2)
    # PrintCollection(Score_jeux3)
    # PrintCollection(Score_jeux4)
    # PrintCollection(Score_jeux5)
    # PrintCollection(Score_jeux6)
    # PrintCollection(Skin)
    
   
    
    
def PrintCollection(Model: object):
    """
        Print collection

        Args:
            Model : model collection to print  
    """
    
    for Element in Model.List:
        print(Element)
    print()

    
    

# code start
if __name__ == "__main__":
    print("\nProjet coconuts/Postgre\n")
    Main()
    print("\nAu revoir\n")