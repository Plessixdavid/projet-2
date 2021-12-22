# coding: utf-8

# imports

import psycopg2

# class
class DBUtil:
    
    Connection = None
    
    @classmethod
    def Connect(
        cls, 
        DBNames : str):
        """
            Connect to named Postgre database
            
            Args :
                DBNames : database name
        """
        
        try:
            cls.Connection = psycopg2.connect(
                user="postgres",
                password="biscotte61",
                host="localhost",
                port="5432",
                database = DBNames)
                    
        except(Exception, psycopg2.Error) as error:
            print(f"Impossible de se connecter à la base Postgre {DBNames}\n{error}")

    @classmethod
    def ExecuteQuery(
        cls,
        Query: str,
        Values: tuple = None) -> list[tuple]:
        """
            Execute specified query

            Args:
                Query : Query to execute
                
            Returns a list of tuples
        """
        DBUtil.Connect("DBNames")

        if cls.Connection is None:
            return

        # get cursor
        Cursor = cls.Connection.cursor()
        
        # execute query
        Cursor.execute(Query, Values)
        
        if Query.startswith("SELECT"):
            Results = Cursor.fetchall()

        else:
            Results = cls.Connection.commit()
        
        # close cursor
        Cursor.close()

        # return results
        return Results

        DBUtil.Close()

    
    @classmethod
    def FillModelCollection(
        cls,
        Query: str,
        Model: object):
        """
            Fill model collection from SQL query
            
            Args :
                Query : SQL query
                Model : model to fill
        """
        
        # get data from query
        Results = cls.ExecuteQuery(Query)  
            
        # create model collection
        for Line in Results:
            Model(Line)

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

    @classmethod
    def Close(cls):
        """
            Free resources
        """
        
        cls.Connection.close()

