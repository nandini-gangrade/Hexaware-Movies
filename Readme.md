# Movies

## Description
This project is a simple application for managing movies. It allows users to perform _CRUD (Create, Read, Update, Delete)_ operations on a database of movies.

## VS Code Setup 

1. Create a folder named "**_Hexaware Movies_**" in VS Code.
2. Inside the folder, create a Python file named "main.py" and write the following code to check if Python is installed correctly:
   
    ```python
    print("hello")
    ```
3. Set up a virtual environment:
   - Open a terminal and navigate to the "**_Hexaware Movies_**" folder.
   - Run the following commands:
     
     ```powershell
     python -m venv myenv
     Set-ExecutionPolicy -Scope Process Bypass
     .\myenv\Scripts\Activate.ps1
     ```
     
4. Create a file named `.gitignore` in the `Hexaware Movies` folder and write "myenv" in it. This will prevent the virtual environment from being tracked by Git.

## Database Setup
To set up the database for the Hexaware Movies application, follow these steps:

- **Create Database**: Create a database named `HexawareMoviesDB` in your preferred database server (e.g., MySQL, PostgreSQL, SQLite).

- **Database Tables**: Create the necessary tables for storing movie data. You can use the Entity-Relationship Diagram (ERD) provided in the project documentation to design the tables. The tables typically include `Movies`, `Directors`, `Actors`, etc., along with their respective attributes. This can be done by executing the `schema.sql` file.

- **Insert Sample Data**: Optionally, you can insert some sample data into the tables to populate the database for testing purposes. This can be done by executing the `seed_data.sql` file.

- **Database Connection**: Update the database connection details in the `DBPropertyUtil.py` file located in the `util` directory. This includes specifying the database server, database name, authentication method, etc.

#### Split into Files

- `schema.sql`: Contains SQL statements to create the database schema and tables.
- `seed_data.sql`: Contains SQL statements to insert sample data into the tables.

## Packages & Files Description
**(In VS Code)**

### `dao`
The `dao` package contains Data Access Object (DAO) classes responsible for interacting with the database. These classes encapsulate the logic for CRUD operations on specific entities.

- `movie_dao.py`: Implements CRUD operations for managing movie data.
- `director_dao.py`: Implements CRUD operations for managing director data.
- `actor_dao.py`: Implements CRUD operations for managing actor data.
- `__init__.py`: Marks the directory as a Python package.

### `entity`
The `entity` package contains entity classes representing the core data objects used in the application. Each entity class typically corresponds to a table in the database.

- `movie.py`: Defines the `Movie` class representing movie entities.
- `director.py`: Defines the `Director` class representing director entities.
- `actor.py`: Defines the `Actor` class representing actor entities.
- `__init__.py`: Marks the directory as a Python package.

### `util`
The `util` package contains utility classes and functions used throughout the application. This includes database connection management and property utilities.

- `DBConnection.py`: Implements the `DBConnection` class responsible for establishing and managing database connections.
- `DBPropertyUtil.py`: Provides utility functions for reading database connection properties.
- `__init__.py`: Marks the directory as a Python package.

### `exceptions`
The `exceptions` package contains custom exception classes for handling errors and input validation in the application.

- `database_exceptions.py`: Defines custom exceptions related to database errors, such as query execution errors and connection errors.
- `input_validation_exceptions.py`: Defines custom exceptions for invalid input data.
- `__init__.py`: Marks the directory as a Python package.

### `main.py`
The `main.py` file is the entry point of the Hexaware Movies application. It contains the main execution logic and user interface for interacting with the application. This file orchestrates the interaction with the DAO classes to perform CRUD operations on movie data.

## Running the Application
To run the **Hexaware Movies** application:

1. Ensure that the database server is running and the `HexawareMoviesDB` database is set up.
2. Activate the virtual environment if not already activated.
3. Navigate to the project directory containing `main.py`.
4. Run the `main.py` file using Python:

   ```powershell
   python main.py
   ```
5. Follow the prompts to perform CRUD operations on the movie database.

## Credits
- This project was created by _[Nandini Gangrade](https://github.com/nandini-gangrade)_
