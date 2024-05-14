import pyodbc
from exceptions.database_exceptions import DatabaseQueryError
from exceptions.input_exceptions import InvalidInputError
from Entity.director import Director

class DirectorDAO:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def create_director(self, director):
        try:
            self.cursor.execute(
                "INSERT INTO Directors (Name) VALUES (?)",
                (director.name,)
            )
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error inserting director into the database") from e

    def read_directors(self):
        try:
            self.cursor.execute("SELECT * FROM Directors")
            directors = []
            for row in self.cursor:
                directors.append(Director(row[1]))  # Assuming columns: Name
            return directors
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error reading directors from the database") from e

    def update_director(self, director_id, updated_director):
        try:
            self.cursor.execute(
                """
                UPDATE Directors
                SET Name = ?
                WHERE DirectorId = ?
                """,
                (updated_director.name, director_id)
            )
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error updating director in the database") from e

    def delete_director(self, director_id):
        try:
            self.cursor.execute("DELETE FROM Directors WHERE DirectorId = ?", (director_id,))
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error deleting director from the database") from e
