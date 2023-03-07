import sqlite3
import os

class database:

    def __init__(self) -> None:
        path = os.path.dirname(os.path.realpath(__file__))
        if not os.path.isfile(path+'\\movie.db'):
            sqlite3.connect('movie.db')
        self.file = 'movie.db'

    def execute_one(self, query):
        try:
            conn = sqlite3.connect(self.file)
            conn.execute(query)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return e

    def get_users(self):
        pass

    def get_movies(self):
        pass
