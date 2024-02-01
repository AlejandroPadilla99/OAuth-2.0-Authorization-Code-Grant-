import sqlite3

connection = None
cursor =  None

def get_db_objects() -> tuple:
    global cursor
    global connection
    if cursor == None and connection:
        connection = sqlite3.connect(database='database.db')
        cursor = connection.cursor()
    return connection, cursor
        