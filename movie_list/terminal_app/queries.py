
create_table_movies = """
CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
year INTEGER,
genre TEXT NOT NULL)"""

create_table_users = """
CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
username TEXT NOT NULL UNIQUE,
password TEXT NOT NULL)
"""

create_table_watched = """
CREATE TABLE IF NOT EXISTS watched
(id INTEGER PRIMARY KEY,
user_id INTEGER NOT NULL,
movie_id INTEGER NOT NULL,
)
"""

select_all_movies = "SELECT * FROM movies"


