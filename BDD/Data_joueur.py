# coding: utf-8

# imports

# class
class Data_joueur:
    """
        Model for Data_joueur table
    """
    
    # class properties
    List = []
    
    # methods
    def __init__(self, 
        ID: int, 
        Name: str, 
        Motdepasse: str, 
        Email: str, 
        SkinID: int,
        ScoreJeux1ID: int,
        ScoreJeux2ID: int,
        ScoreJeux3ID: int ):
        """
            Constructor

            Args:
                ID : primary key
                Name : name
                Image : image URL
                Comment : comments
                CategoryID : foreign key to Category model
        """
        
        self.ID = ID
        self.Name = Name
        self.Motdepasse = Motdepasse
        self.Email = Email
        self.SkinID = SkinID
        self.ScoreJeux1ID = ScoreJeux1ID
        self.ScoreJeux2ID = ScoreJeux2ID
        self.ScoreJeux3ID = ScoreJeux3ID

        
        # add object to collection
        Data_joueur.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}, {self.Name}, {self.Motdepasse}, {self.Email}, (avec l'image {self.SkinID}), {self.ScoreJeux1ID}, {self.ScoreJeux2ID}, {self.ScoreJeux3ID})"
