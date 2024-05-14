import pyodbc
from exceptions.database_exceptions import DatabaseQueryError
from exceptions.input_exceptions import InvalidInputError
from Entity.movie import Movie

class MovieDAO:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def create_movie(self, movie):
        try:
            self.cursor.execute(
                "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
                (movie.title, movie.year, movie.director_id),
            )
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error inserting movie into the database") from e

    def read_movies(self):
        try:
            self.cursor.execute("SELECT * FROM Movies")
            movies = []
            for row in self.cursor:
                movies.append(Movie(row[1], row[2], row[3]))  # Assuming columns: Title, Year, DirectorId
            return movies
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error reading movies from the database") from e

    def update_movie(self, movie_id, updated_movie):
        try:
            self.cursor.execute(
                """
                UPDATE Movies
                SET Title = ?, Year = ?, DirectorId = ?
                WHERE MovieId = ?
                """,
                (updated_movie.title, updated_movie.year, updated_movie.director_id, movie_id),
            )
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error updating movie in the database") from e

    def delete_movie(self, movie_id):
        try:
            self.cursor.execute("DELETE FROM Movies WHERE MovieId = ?", (movie_id,))
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error deleting movie from the database") from e
