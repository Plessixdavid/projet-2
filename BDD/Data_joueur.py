# coding: utf-8

# imports
from Score_jeux1 import Score_jeux1
from Score_jeux2 import Score_jeux2
from Score_jeux3 import Score_jeux3

# class
class Data_joueur:
    """
        Model for Data_joueur table
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
                Name : name
                Image : image URL
                Comment : comments
                CategoryID : foreign key to Category model
        """
        
        # model properties
        self.ID = Data[0]
        self.Name = Data[1]
        self.Motdepasse = Data[2]
        self.Email = Data[3]
        self.SkinID = Data[4]
        self.ScoreJeux1ID = Data[5]
        self.ScoreJeux2ID = Data[6]
        self.ScoreJeux3ID = Data[7]

        
        # calculated properties
        self.Scorejeux1Name = [
            Element.Score 
            for Element 
            in Score_jeux1.List 
            if Element.ID == self.ScoreJeux1ID][0]

        self.Scorejeux2Name = [
            Element.Score 
            for Element 
            in Score_jeux2.List 
            if Element.ID == self.ScoreJeux2ID][0]

        self.Scorejeux3Name = [
            Element.Score 
            for Element 
            in Score_jeux3.List 
            if Element.ID == self.ScoreJeux3ID][0]

        # add object to collection
        Data_joueur.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}, {self.Name}, {self.Motdepasse}, {self.Email}, (avec l'image {self.SkinID}), {self.Scorejeux1Name}, {self.ScoreJeux2ID}, {self.ScoreJeux3ID})"
