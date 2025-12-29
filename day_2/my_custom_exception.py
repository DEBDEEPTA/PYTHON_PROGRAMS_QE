from pyexpat.errors import messages


class AgeValidator(Exception):
    pass  # EXCEPTION WITHOUT ANY CONSTRUCTOR / PARAMETER

class AgeUpperLimitError(Exception):
    def __init__(self, code=505,message="More Than Maximum Age Allowed"):
         self.code = code               # EXCEPTION WITH PARAMETERS WITH DEFAULT VALUES
         self.message = message
         super().__init__(code,message)




class UserValidator(Exception):
    def __init__(self,code,message): # ANY NUMBER OF PARAMETERS CAN BE PASSED TO CONSTRUCTOR & ITS PARENTS SUPER CALL
        self.code = code
        self.message = message
        super().__init__(f"{code} -> {message}")