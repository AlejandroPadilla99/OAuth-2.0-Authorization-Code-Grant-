import sqlite3

connection = sqlite3.connect(database='database.db')

cursor =  None

def get_cursor():
    global cursor
    if cursor == None:
        cursor = connection.cursor()
    return cursor
        