# coding: utf-8

# imports
from Skin import Skin

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
        # self.ScoreJeux1ID = Data[5]
        # self.ScoreJeux2ID = Data[6]
        # self.ScoreJeux3ID = Data[7]
        # self.ScoreJeux4ID = Data[8]
        # self.ScoreJeux5ID = Data[9]
        # self.ScoreJeux6ID = Data[10]

        
        # calculated properties
        self.SkinName = [
            Skin.Element.url_image 
            for Element 
            in Skin.List 
            if Element.ID == self.SkinID][0]

        # add object to collection
        Data_joueur.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}, {self.Name}, {self.Motdepasse}, {self.Email})"
