"""
    1 -> BUILD IN FUNCTIONS

    2 -> USER DEFINED FUNCTIONS
            2.1 -> BASED ON FUNCTION PARAMETERS COMBINATIONS
                2.1.1->
                        1. WITH ARGUMENTS , NO ARGUMENTS                ->
                                                                        -> ALL POSSIBLE COMBINATIONS
                         2. WITH RETURN TYPE, WITHOUT RETURN TYPE       ->

            2.2 -> DEFAULT ARGUMENT FUNCTION

            2.3 -> KEYWORD ARGUMENT FUNCTION

            2.4 -> VARIABLE LENGTH ARGUMENT FUNCTION
                2.4.1 -> *args (NON-KEYWORD VARIABLE ARGUMENT)
                2.4.2 -> **kargs (KEYWORD VARIABLE ARGUMENTS) (TAKES KEY VALUE PAIRS AS INPUT)

            2.5 -> LAMBDA (ANONYMOUS) FUNCTION
                    2.5.1 -> USAGE WITH map()
                    2.5.2 -> USAGE WITH filter()
                    2.5.3 -> USAGE WITH reduce()

            2.6  -> RECURSIVE FUNCTION  (note -> Must have a base Condition)
            2.7  -> GENERATOR FUNCTION
            2.8  -> NESTED FUNCTION
            2.9  -> HIGHER ORDER FUNCTION
            2.10 -> DECORATOR FUNCTION


"""

# FUNCTIONS WITH ARGUMENT
def func_eg(a,b,c):
    sum = a+b+c
    return sum
# FUNCTION WITH ARG NO RETURN
def func_eg(name):
    print("Hello",name)

#FUNCTION WITH DEFAULT VALUES
def func_eg(name="Guest"):
    print("Hello",name)


#KEYWORD ARGUMENT FUNCTION
def fun_eg(name,age):
    print(name,age)

#VARIABLE LENGTH FUNCTION
def var_args_eg(*values):
    """
        *values collects extra positional argument to a function
        inside functon,args behave like a tuple.
        we can iterate over it using for loop to collect the values
        DE-STRUCTURE OF *values -->
            --> a,b,c = values (where number of variables should be exactly same as no.of values passed to the arguments)

    """

    for value in values:
        print(value, end=" ")
    print("TUPLE SPECIFIC METHODS")
    print(f"NUMBER OF VALUES PASSED --> {len(values)}")
    print(f"MAXIMUM VALUE -->{max(values)}")
    print(f"MINIMUM VALUE -->{min(values)}")
    print(f"SUM OF VALUES -->{sum(values)}")

    for i,v in enumerate(values):
        print(f"Value at index {i} --> {v}")

    print()

def var_kargs_eg(**kwargs):
    """
        **kwargs collects extra keyword argument passed to a function
        insdie the function, kwargs is a dictionary
        keys    --> argument names
        values  --> argument values
        the name kwargs is a convention, the ** is mandatory
    """
    print("DICTIONARY -->",kwargs)
    dict_keys = kwargs.keys() # RETURNS LIST OF KEYS
    dict_values = kwargs.values() # RETURN LIST OF VALUES

    print("KEYS ->",dict_keys)
    print("VALUES ->",dict_values)

    for i,v in enumerate(kwargs):
        print(f"INDEX OF THE KEY ->{i} KEY ->{v}")
        #ACESSING VALUES BY KEY
        print("Name ->",kwargs["name"])
        print("Age ->",kwargs["age"])
        print("Active ->",kwargs["active"])

        # ACESSING KEYS & VALUES IN LOOP
        for k,v in kwargs.items():
            print(f"{k} --> {v}")



def main():
    # func_eg("DEV")
    # func_eg(1,2,3)
    #
    # #KEYWORD ARGUMENT FUNC.
    # fun_eg(name="Debdeepta",age=21) # ORDER DOESN'T MATTER
    # var_args_eg(10,20)
    # var_args_eg(10,20,30,40,50,60)
    #var_kargs_eg(a=20,b=30,c=40,d=10)
    var_kargs_eg(name="Dev",age=23,active = True)

# DECORATOR FUNCTION

if __name__=="__main__":
    main()

