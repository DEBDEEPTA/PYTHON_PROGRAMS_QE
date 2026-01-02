"""
                                    #EXCEPTION HANDELING#
        try:
            risky_code
        except ExceptionType:
            handling
        else:
            executes_if_no_exception
        finally:
            always_executes
                                     #EXCEPTION HIERARCHY#
BaseException
 ├── Exception
 │    ├── ValueError
 │    ├── TypeError
 │    ├── ZeroDivisionError
 │    └── IndexError
 ├── SystemExit
 ├── KeyboardInterrupt

 note -> user raise to throw a specific type or custom exception

"""
from day_2.my_custom_exception import AgeValidator, AgeUpperLimitError


def basic_excp():
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    try:
        result = (a / b)
    except Exception as e:  # e(exception object) -> stores type of exception (use to debug)
        print("Something went wrong", e)


def specific_exception():

    """
        (note)
             -> while handling different types of exceptions always go from most specific type of exception
                to general exception
    """
    try:
        a = int(input("Enter value of a\n"))
        b = int(input("Enter value of b\n"))
        result = a/b
    except ZeroDivisionError as e:
        print("Divide by Zero error block ->",e)
    except ValueError as e:
        print("Value error block ->",e)
    except Exception as e:
        print("General exception block ->",e)
    else:       # else block executes if no exception occurred
        print(result)
    finally:    # finally block executes no matter what kind of exception has occurred
        print("finally block executed")


def multi_excep():
    """
        HANDELING MULTIPLE DIFFERENT TYPE OF EXCEPTION IN A SINGLE EXCEPT BLOCK
    """
    try:
        a = int(input("Enter value of a\n"))
        b = int(input("Enter value of b\n"))
        result = (a/b)
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print("Error Type -> ",e)
    else:
        print(result)
    finally:
        print("finally block executed")

def throwing_excep():
    """
        raise keyword is used to manually trigger exception
        simillar to throwing exception in java
    """
    try:
        age = int(input("Enter age -> "))
        if (age < 18):
            raise RuntimeError("Invalid Age")
    except Exception as e:
        print("Exception occured -> ",e)
    else:
        print(f"Your age -> {age}")


"""
            ************************ EXCEPTION PROPAGATION IN PYTHON ***************************
"""

def exp_prop(num_a, num_b):
    try:
        result = divide(num_a, num_b)
    except Exception as e:
        print("Exception Caught at exp_prop() ->",e)
    else:
        return result

def divide(a,b):
    try:
        result = (a/b)
    except Exception as e:
        print("Exception occurred at divide()")
        # raise
        # or
        raise Exception("Exception propagates to upper Layer") from e # WILL SEND THIS EXCEPTION MESSAGE
        """ 
                will throw (re-raise) exception to its calling class, and propagates upwards in function call stack
                ie.,  divide() ---re-raise---> exp_prop()
         """
    else:
        return result


"""
                ********************* HANDELING CUSTOM EXCEPTION *************************** 
"""


import my_custom_exception

def custom_exp_age():

    try:
        age = int(input("Enter your age\n"))
        if (age < 18):
            raise AgeValidator("Invalid Age")
        if(age > 75):
            raise  AgeUpperLimitError(message="Should be less than 75")
    except (AgeValidator,AgeUpperLimitError) as e:
        print("Exception type ->",e)



def main():
    #basic_excp()
    #specific_exception()
    #multi_excep()
    #throwing_excep()
    #exp_prop(5,0)
    custom_exp_age()




if __name__ =="__main__":
    main()
