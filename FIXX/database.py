import sqlite3
import os

class getDatabase:
    def __init__(self):
        self.database= sqlite3.connect('project.sqlite')
        self.cursor = self.database.cursor()

    def deleteScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')