class TokenIsMissingException(Exception):
    def __init__(self):
        self.message = "Token doesn't exist."
        super().__init__(self.message)