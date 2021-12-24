# coding: utf-8

# imports


# class
class Skin:
    """
        Model for Skin table
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
                Url_image : image
                
        """
        
        # model properties
        self.ID = Data[0]
        self.Url_image = Data[1]
       
        
        # calculated properties
       
        # add object to collection
        Skin.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}, {self.Url_image})"