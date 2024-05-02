"""File to create the table in database for the first time"""
import sqlite3

DATA_BASE_NAME =  "data_base.db"
SCHEMA_FILE = "schema.sql"

#Global connection and cursor
_connection = sqlite3.connect(DATA_BASE_NAME)

def execute_schema():
    """Function to execute the table's schema"""
    with open(SCHEMA_FILE,encoding="utf-8") as file:
        _connection.executescript(file.read())

#execute_schema()
_connection.close()
