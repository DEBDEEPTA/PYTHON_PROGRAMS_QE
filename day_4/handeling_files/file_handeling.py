# ******************** FILE HANDELING *******************
""" Open File
    syntax -> file_object_name = open("file_path", "mode")
    open() -> returns a file object
    note -> best practise (open read file using "with" keyword
"""
file_obj1 = open("sample.txt", 'r')  # open file in read mode
file_obj1.close() # If you don’t close a file:
                  # Memory leak
                  # File may not be saved properly
file_obj2 = open("sample.txt", "rb") # opened in read & binary mode
file_obj2.close() # closing file

# BEST PRACTISE TO CLOSE A FILE (AUTOMATIC)
with open("sample.txt", "r") as file_object_a:
    print("Inside The Scope of the With")
    content = file_object_a.read()
# AUTOMATICALLY CLOSED WHEN SCOPE IS OUTSIDE THE With BLOCK




""" Reading a File
        -> Reading Whole File
        -> Reading N Characters form the file
        -> Read OneLine from the file
        -> Read AllLines From the file -> (returns List of Lines with "\n" append to each line except last)
        -> Reading with Loops 
"""

""" Reading Whole File
    syntax =>   file_object_name.read()
"""

with open("sample.txt", "r") as file_obj_a:
     print("Read whole File")
     print(file_obj_a.read())

""" Reading N Characters 
    syntax =>   file_object_name.read()
"""
with open("sample.txt", "r") as file_obj_b:
    N = 10
    print(f"Read {N} Characters")
    print(file_obj_b.read(N))

""" Reading Single Line 
    syntax =>   file_object_name.readline()
"""
with open("sample.txt", "r") as file_obj_c:
    print(f"Reading Single Line")
    print(file_obj_c.readline())

""" Reading Multiple Line 
    syntax =>   file_object_name.readlines()
"""

with open("sample.txt", "r") as file_obj_d:
    print(f"Reading All Line")
    print(file_obj_d.readlines())

""" Reading using Loops"""
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())



"""" Appending File """

with open("sample.txt", "a") as f:
    f.write("New Line Added\n")