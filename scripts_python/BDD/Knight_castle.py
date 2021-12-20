# coding: utf-8

# imports
from Data_joueur import Data_joueur

# class
class Knight_castle:
    """
        Model for Knight_castle table
    """
    
    # class properties
    List = []
    
    # methods
    def __init__(self, 
        Data: tuple):
        """
            Constructor

            Args:
                ID : primary key
                Score : Score
                NameID : name ID
               l
        """
        
        # model properties
        self.ID = Data[0]
        self.Score = Data[1]
        self.NameID = Data[2]
        
        
        # calculated properties
        self.names = [
            Element.Name
            for Element 
            in Data_joueur.List 
            if Element.ID == self.NameID][0]
        

        # add object to collection
        Knight_castle.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}, {self.Score}, {self.names})"