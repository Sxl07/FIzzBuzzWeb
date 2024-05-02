"""File to manage SQL sentences for work in database"""
import sqlite3
from .i_data_storage import IDataStorage #pylint: disable=E0402
from .data_base import DATA_BASE_NAME #pylint: disable=E0402

class DBStorage(IDataStorage):
    """Class to connect the database and work on it"""
    def __init__(self) -> None:
        pass
    @staticmethod
    def get_db_connection():
        """Method to stablish connection with the database"""
        conn = sqlite3.connect(DATA_BASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    def get_num(self,number):
        """Method to make a request for a number in the database"""
        conn=self.get_db_connection()
        result = conn.execute("SELECT num, fizzbuzz FROM numbers WHERE num = ? ", (number,)).fetchone()
        conn.close()
        return result
    def get_active(self, number):
        """Method to check if a number is active in the database"""
        conn =self.get_db_connection()
        result = conn.execute("SELECT num, fizzbuzz FROM numbers WHERE num=? AND active='1'", (number,)).fetchone()
        conn.close()
        return result
    def insert_new_number(self, number):
        """Method to insert a new number in the database"""
        conn =self.get_db_connection()
        conn.execute("INSERT INTO numbers (num, fizzbuzz, active) VALUES (?, ?, 1)",(number[0],number[1]))
        conn.commit()
        conn.close()
    def activate_num(self, number):
        """Method to activate a number in the database"""
        conn=self.get_db_connection()
        conn.execute("UPDATE numbers SET active = '1' WHERE num=?", (number,))
        conn.commit()
        conn.close()
    def deactivate_num(self, number):
        """Method to deactivate a number in the database"""
        conn=self.get_db_connection()
        conn.execute("UPDATE numbers SET active = '0' WHERE num = ?",(number,))
        conn.commit()
        conn.close()
    def get_range(self, min_limit,max_limit):
        """Method to make a request for a range of numbers"""
        conn=self.get_db_connection()
        result = conn.execute("SELECT * FROM numbers WHERE num BETWEEN ? AND ? AND active = '1'",(min_limit,max_limit)).fetchall()
        conn.close()
        return result
