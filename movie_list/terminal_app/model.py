import sqlite3
import functools
import os
import queries


class database:

    def __init__(self) -> None:
        self.dbfile = 'movies_app.db'
        if not os.path.isfile(self.dbfile):
            sqlite3.connect(self.dbfile)
            self.initialize_db()

    def with_db(func):
        @functools.wraps(func)
        def dbconn_wrapper(self, query):
            with sqlite3.connect(self.dbfile) as conn:
                cursor = conn.cursor()
                result = func(cursor, query)
                cursor.close()
            return result
        return dbconn_wrapper


    def initialize_db(self) -> bool:
        try:
            self.exec_only(queries.create_table_movies)
            # Add here other actions needed to init the db
        except Exception as e:
            return e


    @with_db
    def exec_only(self, cursor, query) -> None:
        cursor.execute(query)
        return


    @with_db
    def exec_fetchall(self, cursor, query) -> str:
        cursor.execute(query)
        query_result = cursor.fetchall  
        return query_result
    
