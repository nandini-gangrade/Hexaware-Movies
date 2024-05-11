import pyodbc  # Importing the pyodbc library for database connectivity

# Server and database information
server_name = "DESKTOP-K702Q3Q\SQLEXPRESS09"  # Server name where the database is hosted
database_name = "HexawareMoviesDB"  # Name of the database

# Connection string for establishing a connection to the database
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

# Printing connection string for reference
print(conn_str)

# Establishing connection to the database
conn = pyodbc.connect(conn_str)  # Establishing connection using the connection string
cursor = conn.cursor()  # Creating a cursor object to execute SQL queries

# Executing a sample query to check if the connection is successful
cursor.execute("Select 1")  # Executing a simple query
print("DB connection is successful🎉")  # Printing success message if connection is successful


# Function to create a new movie entry in the database
def create_movie():
    Title = input("Enter the title of the movie: ")  # Prompting user to enter movie title
    Year = int(input("Enter the year of release: "))  # Prompting user to enter movie release year
    DirectorId = int(input("Enter the director ID: "))  # Prompting user to enter director ID

    # Executing query to insert a new movie record into the database
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        Title, Year, DirectorId,
    )
    conn.commit()  # Committing the transaction
    print("Movie created successfully.")  # Printing success message


# Function to read movies from the database
def read_movies():
    cursor.execute("Select * from Movies")  # Executing query to select all movies
    for row in cursor:
        print(row)  # Printing each row fetched from the database


# Function to update details of a movie in the database
def update_movie():
    movie_id = int(input("Enter the Movie_Id to be updated: "))  # Prompting user to enter movie ID to be updated
    new_title = input("Enter the new title of the movie: ")  # Prompting user to enter new movie title
    new_year = int(input("Enter the new year of release: "))  # Prompting user to enter new movie release year
    new_director_id = int(input("Enter the new director ID: "))  # Prompting user to enter new director ID

    # Executing query to update the details of the specified movie record in the database
    cursor.execute(
        "UPDATE Movies SET Title = ?, Year = ?, DirectorId = ? WHERE MovieId = ?",
        new_title, new_year, new_director_id, movie_id,
    )
    conn.commit()  # Committing the transaction
    print("Movie updated successfully.")  # Printing success message


# Function to delete a movie from the database
def delete_movie():
    movie_id = int(input("Enter the Movie_Id to be deleted: "))  # Prompting user to enter movie ID to be deleted
    # Executing query to delete the specified movie record from the database
    cursor.execute("DELETE FROM Movies WHERE MovieId = ?", movie_id)
    conn.commit()  # Committing the transaction
    print("Movie deleted successfully.")  # Printing success message


# Main function to run the application
if __name__ == "__main__":
    print("\nWelcome to the Movies Application🎉")
    while True:
        print("\n1. Create Movie")  # Option to create a new movie entry in the database
        print("2. Read Movies")  # Option to read movies from the database
        print("3. Update Movie")  # Option to update details of an existing movie in the database
        print("4. Delete Movie")  # Option to delete a movie from the database
        print("5. Exit")  # Option to exit the application

        choice = input("\nEnter your choice: ")  # Prompting user to enter their choice

        if choice == "1":
            create_movie()  # Calling function to create a new movie
        elif choice == "2":
            read_movies()  # Calling function to read movies
        elif choice == "3":
            update_movie()  # Calling function to update a movie
        elif choice == "4":
            delete_movie()  # Calling function to delete a movie
        elif choice == "5":
            break  # Exiting the loop if choice is '5'
        else:
            print("Invalid choice. Please enter a valid option.")  # Error message for invalid input
