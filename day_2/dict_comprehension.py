"""
    Dictionary comprehension is used to create dictionaries in a single line.
    Why use it?
        -> Cleaner syntax
        -> Faster dictionary creation
        -> Easy transformation of data
    Syntax
        -> {key_expression: value_expression for item in iterable}

"""

def normal_dict():
    squares = {}
    for i in range(5):
   #    key <-----> value
        squares[i] = i*i
    print(squares) # {0:0, 1:1 , 2:4, 3:9, 4:16}

def dict_comperhension():
      #         key :   value
    squares = {  i  :   i*i for i in range(5)}
    print(squares)

def dict_comperhension_io():
    """
        ->   _ means loop variable is not needed
        ->   Common Python convention
    """
    n = int(input("Enter number of elements\n"))
    squares = {int(input("Enter Key -> ")): int(input("Enter value -> ")) for _ in range(n)}
    print(squares)

def main():
    #normal_dict()
    #dict_comperhension()
    dict_comperhension_io()

if __name__ == "__main__":
    main()

