# Hexaware Movies

## Description
This project is a simple application for managing movies. It allows users to perform CRUD (Create, Read, Update, Delete) operations on a database of movies.

## Setup Instructions

1. Create a folder named "Hexaware Movies" in VS Code.
2. Inside the folder, create a Python file named "main.py" and write the following code to check if Python is installed correctly:
   
    ```python
    print("hello")
    ```
4. Set up a virtual environment:
   - Open a terminal and navigate to the "Hexaware Movies" folder.
   - Run the following commands:
     
     ```bash
     python -m venv myenv
     Set-ExecutionPolicy -Scope Process Bypass
     .\myenv\Scripts\Activate.ps1
     ```
5. Create a file named ".gitignore" in the "Hexaware Movies" folder and write "myenv" in it. This will prevent the virtual environment from being tracked by Git.
6. Create an Entity-Relationship Diagram (ERD) to design the tables for storing movie data. Define tables such as Movies, Directors, Genres, etc., and their relationships.
7. Set up a database and connect to the server using SQL Server Management Studio (SSMS). Create the "HexawareMoviesDB" database and create tables based on the ERD. Insert some sample values into the tables.
8. Install the pyodbc library in Visual Studio Code by running the following command in the terminal:
   
    ```bash
    pip install pyodbc
    ```
10. In the "main.py" file, establish a connection to the database using pyodbc and perform CRUD operations on the movie data.

## Usage
- Run the "main.py" file to start the application.
- Follow the prompts to perform CRUD operations on the movie database.

## Credits
- This project was created by [Nandini Gangrade](https://github.com/nandini-gangrade)
