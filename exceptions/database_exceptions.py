class DatabaseQueryError(Exception):
    """Exception raised for errors in database queries."""

    def __init__(self, message="Error executing database query"):
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionError(Exception):
    """Exception raised for errors in database connection."""

    def __init__(self, message="Error connecting to the database"):
        self.message = message
        super().__init__(self.message)

