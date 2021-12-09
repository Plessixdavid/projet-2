# coding: utf-8

# imports
from DBUtil import DBUtil
from Data_joueur import Data_joueur
from Score_jeux1 import Score_jeux1


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("Projet coconuts")
    
  # get categories
    DBUtil.FillModelCollection("SELECT * FROM Score_jeux1", Score_jeux1)
    DBUtil.FillModelCollection("SELECT * FROM Data_joueur", Data_joueur)
    # DBUtil.FillModelCollection("SELECT * FROM Score_jeux2", Score_jeux2)
    # DBUtil.FillModelCollection("SELECT * FROM Score_jeux3", Score_jeux3)

        
      # close DB
    DBUtil.Close()
  
    # print model content
    PrintCollection(Data_joueur)
    PrintCollection(Score_jeux1)
    
   
    
    
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