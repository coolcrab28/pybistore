"""
Create database and tables
>>> from app import *
"""

import pickle
from os.path import exists

class Database():
    """
    create a database
    >>> db = Database()
    """

    name:str = "" 
    def __init__(self):
        pass
    def __int__(self):
        return None
    def __str__(self)->None:
        return "None"
    def use(self,name):
        try:
            if exists(f"db/{name}/"):
                self.name = name
                print("great")
            else:
                print("\033[91m[error]\033[00m No such database was found! Please create a new one or use an existing one")
        except:
            print("\033[91m[error]\033[00m Something went wrong!")
