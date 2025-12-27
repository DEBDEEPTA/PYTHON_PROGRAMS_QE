"""
    List comprehension is a short and readable way to create lists in Python.
    It replaces traditional for loops that build lists one element at a time.

    Features
        ->Less code
        -> More readable
        -> Often faster than loops
        -> Expresses logic clearly in one line

    syntax
        -> [expression for item in iterable]
"""

def normal_list():  # CREATING LIST USING FOR LOOP
    my_list = []
    for i in range(1,6):
        my_list.append(i)
    print(my_list)  # [1,2,3,4,5]

def comperh_list(): #CREATING LIST USING LIST COMERHENSION
    my_list = [i for i in range(1,6)]
    print(my_list)  #[1,2,3,4,5]


def comperh_list_user_io():
    """
        TAKING USER INPUT USING LIST COMPREHENSION
    """
    n = int(input("Enter the number of elements\n"))
    my_list = [int(input(f"Enter the element{i+1} -> ")) for i in range(n)]
    print(my_list)

def comperh_list_user_io_single_line():
    """
        TAKING USER INPUT IN A SINGLE LINE USING LIST COMPREHENSION
    """
    my_list = [int(i) for i in input("ENTER THE ELEMENTS SEPARATED BY SPACE\n").split()]
    print(my_list)

def comperh_list_condition():
    result = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
    print(result) # ['Even', 'Odd', 'Even', 'Odd', 'Even']

def main():
    # normal_list()
    # comperh_list()
    # comperh_list_condition()
    # comperh_list_user_io()
    comperh_list_user_io_single_line()
if __name__ == "__main__":
    main()