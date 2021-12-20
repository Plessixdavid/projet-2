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
                SkinID : image ID
                Motdepasse : password
                Email : Email
        """
        
        # model properties
        self.ID = Data[0]
        self.Motdepasse = Data[1]
        self.Email = Data[2]
        self.SkinID = Data[3]
        self.Name = Data[4]
        
        # calculated properties
        self.Skinname = [
            Element.Url_image 
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

        return f"({self.ID}, {self.Name}, {self.Motdepasse}, {self.Email}, {self.Skinname})"
