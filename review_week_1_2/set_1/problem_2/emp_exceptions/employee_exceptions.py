class EmailError(Exception):
    def __init__(self, message = "Invalid Email"):
        self.message = message
        super().__init__(message)


class PhoneError(Exception):
    def __init__(self, message = "Invalid Phone Number"):
        self.message= message
        super().__init__(message)

