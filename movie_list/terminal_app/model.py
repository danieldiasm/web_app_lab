import sqlite3
import os
import queries


class database:

    def __init__(self) -> None:
        self.dbfile = 'movies_app.db'
        if not os.path.isfile(self.dbfile):
            sqlite3.connect(self.dbfile)
            self.initialize_db()
       

    def initialize_db(self) -> bool:
        if database.execute(self, queries.create_table_movies):
            return True
        else:
            raise Exception("Failed creating tables, sorry.")

    def execute(self, query):
        with sqlite3.connect(self.dbfile) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(query)
                except Exception as e:
                    raise f"Something went wrong:{e}"
                    return False
                cursor.close()
        return True
    
    def fetch_all(self, query):
        with sqlite3.connect(self.dbfile) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(query)
                    result = cursor.fetchall()
                except Exception as e:
                    raise f"Something went wrong:{e}"
                    return False
                cursor.close()
        return result
