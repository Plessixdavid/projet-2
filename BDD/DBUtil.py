# coding: utf-8

# imports
import psycopg2

# class
class DBUtil:
    
    Connection = None
    
    @classmethod
    def Connect(
        cls, 
        DBName : str):
        """
            Connect to named Postgre database
            
            Args :
                DBName : database name
        """
        
        try:
            cls.Connection = psycopg2.connect(
                user="postgres",
                password="azerty",
                host="localhost",
                port="5432",
                database=DBName)
                    
        except(Exception, psycopg2.Error) as error:
            print(f"Impossible de se connecter à la base Postgre {DBName}\n{error}")


    @classmethod
    def ExecuteQuery(
        cls,
        Query: str) -> list[tuple]:
        """
            Execute specified query

            Args:
                Query : Query to execute
                
            Returns a list of tuples
        """

        if cls.Connection is None:
            return

        # get cursor
        Cursor = cls.Connection.cursor()
        
        # execute query
        Query = Query
        Cursor.execute(Query)
        Results = Cursor.fetchall()

        # return results
        return Results


    @staticmethod
    def PrintResults(
        Results: list[tuple], 
        Separator: str = ", "):
        """
            Print list of tuples

            Args:
                Results : data to print
                Separator : separator for tuples
        """
        
        if Results is None:
            return

        for Line in Results:
            for Data in Line:
                print(f"{Data}{Separator}", end="")
            print()
