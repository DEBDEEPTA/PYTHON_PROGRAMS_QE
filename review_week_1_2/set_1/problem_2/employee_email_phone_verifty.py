from review_week_1_2.set_1.problem_2.emp_exceptions.employee_exceptions import EmailError, PhoneError
from review_week_1_2.set_1.problem_2.validators.employee_validators import validate_email, validate_phone

class Employee:
    def __init__(self,id_val,name_val,email_val,phone_val):
        self.id = id_val
        self.name = name_val
        self.email = email_val
        self.phone = phone_val


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,emp_id):
        self.__id = emp_id

    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self,emp_name):
        self.__name = emp_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,emp_email):
        if (validate_email(emp_email)):
            self.__email = emp_email
        else:
            raise EmailError()



    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,emp_phone):
        if (validate_phone(emp_phone)):
            self.__phone = emp_phone
        else:
            raise PhoneError()


    def __str__(self):
        return f"[id:{self.id}\nname:{self.name}\nemail:{self.email}\nphone:{self.phone}]"

if __name__ == "__main__":

    try:
        ev1 = Employee("05JAN26", "DEV", "deep@gmail.com", "8001332960")  # VALID
        print(ev1)
        ev2 = Employee("05JAN26", "MAX", "max2003@gmail.com", 8001334960)  # VALID
        print(ev2)

        e2 = Employee("06JAN26", "AVI", ".avi@", "123444")  # RAISE EMAIL & PHONE ERROR

        e3 = Employee("07JAN26", "SID", "sid.26@co.in", 1234567891)  # RAISE INVALID PHONE NUMBER
    except EmailError as e:
        print(e)
    except PhoneError as e:
        print(e)

