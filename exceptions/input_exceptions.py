class InvalidInputError(Exception):
    """Exception raised for invalid input."""

    def __init__(self, input_name, message="Invalid input"):
        self.input_name = input_name
        self.message = f"{message}: {input_name}"
        super().__init__(self.message)
