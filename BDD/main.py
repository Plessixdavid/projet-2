# coding: utf-8

# imports
from DBUtil import DBUtil
from Data_joueur import Data_joueur


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("Projet coconuts")
    
    # get vegetals
    Query = "SELECT * FROM Data_joueur"
    Results = DBUtil.ExecuteQuery(Query)
        
    # create vegetal collection
    for Line in Results:
        Data_joueur(
            Line[0], 
            Line[1], 
            Line[2], 
            Line[3], 
            Line[4],
            Line[5],
            Line[6],
            Line[7],)
    
    # print model content
    for Element in Data_joueur.List:
        print(Element)
             
    
    

# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir\n")