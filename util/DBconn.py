import pyodbc
from util import DBPropertyUtil
from exceptions.database_exceptions import DatabaseConnectionError

class DBConnection:
    def __init__(self):
        try:
            conn_str = DBPropertyUtil.PropertyUtil.get_property_string()
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            raise DatabaseConnectionError("Error connecting to the database") from e

    def close(self):
        self.cursor.close()
        self.conn.close()
