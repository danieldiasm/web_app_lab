
create_table_movies = """
CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
year INTEGER,
genre TEXT NOT NULL)"""

select_all_movies = "SELECT * FROM movies"


