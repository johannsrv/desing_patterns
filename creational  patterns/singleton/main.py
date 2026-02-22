"Singleton Design Pattern Example in Python"

"""
The Singleton design pattern is a software design pattern that restricts the instantiation of a class to a single
instance and provides a global point of access to that instance. This is useful when exactly one object is needed to coordinate actions across the system.
In this example, we implement the Singleton pattern using a class variable to store the single instance of the class. The __new__ method is overridden to control the instantiation process and ensure that only one instance of the class is created.
"""

class Singleton:
    __instance =  {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__new__(cls)
        return cls.__instance[cls]


# Testing the Singleton implementation 
#  Create 2 instances of the Singleton class and check if they are the same instance. 
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True


# Example using the Singleton class to manage a database connection sqlite3
import sqlite3

class DatabaseConnection(Singleton):
    conection = None

    def __init__(self) -> None:
        if self.conection is None:
            self.conection = sqlite3.connect('users.db')

    def execute_query(self, query: str) -> None:
        cursor = self.conection.cursor()
        cursor.execute(query)
        self.conection.commit()

    def close_connection(self) -> None:
        self.conection.close()
    

# Create a instance of the DatabaseConnection class and execute a query to create a table. Then, create another instance and check if it is the same instance as the first one. Finally, close the database connection.
db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Alice')")

db2.close_connection()
db1.close_connection()