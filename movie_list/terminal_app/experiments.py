import model
import queries
dbhandler = model.database()
print(dbhandler.execute(queries.create_table_movies))

print(dbhandler.fetch("SELECT * FROM sqlite_master WHERE type='table'"))