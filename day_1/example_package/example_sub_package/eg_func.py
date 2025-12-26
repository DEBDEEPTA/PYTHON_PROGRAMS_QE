
def add_nums(*values):
    total = sum(values)
    return total

def mul_nums(*values):
    total = 1
    for v in values:
        total *= v
    return total



def main():
    print("Running Directly From eg_func.py")
    print(add_nums(5, 4, 3))
    print(mul_nums(5, 4, 3))

if __name__ == "__main__":
    main()