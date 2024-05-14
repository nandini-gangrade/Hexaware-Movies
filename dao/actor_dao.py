import pyodbc
from exceptions.database_exceptions import DatabaseQueryError
from exceptions.input_exceptions import InvalidInputError
from Entity.actor import Actor

class ActorDAO:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def create_actor(self, actor):
        try:
            self.cursor.execute(
                "INSERT INTO Actors (Name) VALUES (?)",
                (actor.name,)
            )
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error inserting actor into the database") from e

    def read_actors(self):
        try:
            self.cursor.execute("SELECT * FROM Actors")
            actors = []
            for row in self.cursor:
                actors.append(Actor(row[1]))  # Assuming columns: Name
            return actors
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error reading actors from the database") from e

    def update_actor(self, actor_id, updated_actor):
        try:
            self.cursor.execute(
                """
                UPDATE Actors
                SET Name = ?
                WHERE ActorId = ?
                """,
                (updated_actor.name, actor_id)
            )
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error updating actor in the database") from e

    def delete_actor(self, actor_id):
        try:
            self.cursor.execute("DELETE FROM Actors WHERE ActorId = ?", (actor_id,))
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error deleting actor from the database") from e
