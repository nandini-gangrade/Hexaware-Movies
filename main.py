import pyodbc
from dao import MovieDAO, DirectorDAO, ActorDAO
from Entity import Movie, Director, Actor
from util import DBConnection
from exceptions.database_exceptions import DatabaseQueryError, DatabaseConnectionError
from exceptions.input_exceptions import InvalidInputError

def main():
    print("Welcome to the movies app")

    try:
        # Establish database connection
        db_connection = DBConnection()

        # Create DAO instances
        movie_dao = MovieDAO(db_connection.conn, db_connection.cursor)
        director_dao = DirectorDAO(db_connection.conn, db_connection.cursor)
        actor_dao = ActorDAO(db_connection.conn, db_connection.cursor)

        while True:
            print(
                """      
                1. Movie Management
                2. Director Management
                3. Actor Management
                4. Exit
                    """
            )

            choice = int(input("Please choose from above options: "))

            if choice == 1:
                movie_menu(movie_dao)
            elif choice == 2:
                director_menu(director_dao)
            elif choice == 3:
                actor_menu(actor_dao)
            elif choice == 4:
                break

    except DatabaseConnectionError as e:
        print(f"Error: {e.message}")

    finally:
        # Close database connection
        if 'db_connection' in locals():
            db_connection.close()

def movie_menu(movie_dao):
    while True:
        print(
            """      
            Movie Management Menu:
            1. Add a Movie
            2. View all Movies
            3. Update a Movie  
            4. Delete a Movie
            5. Back to main menu
            """
        )
        choice = int(input("Please choose from the options above: "))

        try:
            if choice == 1:
                title = input("Please enter movie title: ")
                year = int(input("Please enter movie year: "))
                director_id = int(input("Please enter movie director's id: "))
                new_movie = Movie(title, year, director_id)
                movie_dao.create_movie(new_movie)
            elif choice == 2:
                movies = movie_dao.read_movies()
                for movie in movies:
                    print(movie.__dict__)
            elif choice == 3:
                movie_id = int(input("Please enter movie ID to update: "))
                title = input("Please enter updated movie title: ")
                year = int(input("Please enter updated movie year: "))
                director_id = int(input("Please enter updated movie director's id: "))
                updated_movie = Movie(title, year, director_id)
                movie_dao.update_movie(movie_id, updated_movie)
            elif choice == 4:
                movie_id = int(input("Please enter movie ID to delete: "))
                movie_dao.delete_movie(movie_id)
            elif choice == 5:
                break
        except InvalidInputError as e:
            print(f"Invalid input: {e.input_name}")
        except DatabaseQueryError as e:
            print(f"Database query error: {e.message}")

def director_menu(director_dao):
    while True:
        print(
            """      
            Director Management Menu:
            1. Add a Director
            2. View all Directors
            3. Update a Director  
            4. Delete a Director
            5. Back to main menu
            """
        )
        choice = int(input("Please choose from the options above: "))

        try:
            if choice == 1:
                name = input("Please enter director's name: ")
                new_director = Director(name)
                director_dao.create_director(new_director)
            elif choice == 2:
                directors = director_dao.read_directors()
                for director in directors:
                    print(director.__dict__)
            elif choice == 3:
                director_id = int(input("Please enter director ID to update: "))
                name = input("Please enter updated director's name: ")
                updated_director = Director(name)
                director_dao.update_director(director_id, updated_director)
            elif choice == 4:
                director_id = int(input("Please enter director ID to delete: "))
                director_dao.delete_director(director_id)
            elif choice == 5:
                break
        except InvalidInputError as e:
            print(f"Invalid input: {e.input_name}")
        except DatabaseQueryError as e:
            print(f"Database query error: {e.message}")

def actor_menu(actor_dao):
    while True:
        print(
            """      
            Actor Management Menu:
            1. Add an Actor
            2. View all Actors
            3. Update an Actor  
            4. Delete an Actor
            5. Back to main menu
            """
        )
        choice = int(input("Please choose from the options above: "))

        try:
            if choice == 1:
                name = input("Please enter actor's name: ")
                new_actor = Actor(name)
                actor_dao.create_actor(new_actor)
            elif choice == 2:
                actors = actor_dao.read_actors()
                for actor in actors:
                    print(actor.__dict__)
            elif choice == 3:
                actor_id = int(input("Please enter actor ID to update: "))
                name = input("Please enter updated actor's name: ")
                updated_actor = Actor(name)
                actor_dao.update_actor(actor_id, updated_actor)
            elif choice == 4:
                actor_id = int(input("Please enter actor ID to delete: "))
                actor_dao.delete_actor(actor_id)
            elif choice == 5:
                break
        except InvalidInputError as e:
            print(f"Invalid input: {e.input_name}")
        except DatabaseQueryError as e:
            print(f"Database query error: {e.message}")

if __name__ == "__main__":
    main()
