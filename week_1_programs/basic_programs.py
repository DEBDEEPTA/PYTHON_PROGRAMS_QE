#                                   BASIC PROGRAMS
import random

def task_1():
    """
         1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
             a. I/P-> Take User Name as Input.Ensure UserName has min 3 char
             b. Logic -> Replace <<UserName>> with the proper name
             c. O/P -> Print the String with User Name
    """

    user_input = input('Enter your name:\n')
    if (len(user_input) < 3):
          print("UserName should be at least 3 characters Long")
    if (len(user_input) >= 3):
        # Using formated String PlaceHolder
        print(f"Hello {user_input},How are you?")

        # Using Format Method
        # print("Hello {},How are you?".format(user_input))

        # Using C Style PlaceHolder
        # print("Hello %s,How are you?" % user_input)
        # Using String Concatenation
        # print("Hello " + user_input + ",How are you?")


def task_2():
    """
    2. Flip Coin and print percentage of Heads and Tails.
        a. I/P -> The number of times to Flip Coin.Ensure it is positive integer.
        b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
                    heads.
        c. O/P -> Percentage of Head vs Tails
    """

    user_input = int(input("Enter the Number of times the coin is flipped\n"))
    if not (user_input>=1):
        print("Value should be a positive number")
    else:
        h = 0
        t = 0
        for i in range(user_input):
            coin_range = random.Random().uniform(0.0, 1.0)
            #print(coin_range) # to debug
            if (coin_range < 0.5):
                t += 1
            else:
                h += 1

        t_percentage = (t/user_input)*100
        h_percentage = (h/user_input)*100
        print(f"percentage Of Head occurance: {t_percentage}\n"
              f"percentage of Tail occurance: {h_percentage}")


def task_3():
    """
       3. Leap Year.
           a. I/P -> Year, ensure it is a 4 digit number.
           b. Logic -> Determine if it is a Leap Year.
           c. O/P -> Print the year is a Leap Year or not.
    """
    year = int(input("Enter a year\n"))
    if not (len(str(year)) == 4):
        print("Invalid year, must be 4 digit")
    else:
        if(year % 100 == 0): # Checking if the year is century
            if(year % 400 == 0):
                print(f"{year} is leap year")
            else:
                print(f"{year} is not a leap year")

        elif(year % 4 == 0): # For not century years
            print(f"{year} is leap year")

        else:
            print(f"{year} is not a leap year")

def task_4():
    """
        4. Power of 2
            a. Desc -> This program takes a command-line argument N and prints a table of the
                        powers of 2 that are less than or equal to 2^N.
            b. I/P -> The Power Value N.Only works if 0 <= N < 31 since 2^31 overflows an int
            c. Logic -> repeat until i equals N.
    """
    power = int(input("Enter power value\n"))
    if not (0<=power<31):
        print("Invalid Input")

    flag = True
    index = 0
    while(flag):
        value = pow(2,index)
        print(f"2^{index} --> {value}")
        index += 1
        if(index == power):
            flag = False

def task_5():
    """
        5. Harmonic Number
            a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
                        (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
            b. I/P -> The Harmonic Value N.Ensure N != 0
            c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
            d. O/P -> Print the Nth Harmonic Value.
    """
    value = int(input("Enter the value\n"))
    if(value == 0):
        print("Invalid Input")
    else:
        sum = 0
        for i in range(1, value+1):
            sum += (1/i)
        print(sum)

def task_6():
    """
        6. Factors.
            a. Desc -> Computes the prime factorization of N using brute force.
            b. I/P -> Number to find the prime factors
            c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
            d. O/P -> Print the prime factors of number N.
    """
    set_temp = set(); # EMPETY SET TO STROE THE PRIMEFACTORS AND IGNORING DUPLICATES
    def find_prime(value,min_divisor):
        if value <= 1:
            return
        if value % min_divisor == 0:
            set_temp.add(min_divisor)
            find_prime(value//min_divisor, min_divisor)
        else:
            find_prime(value,min_divisor+1)

    value = int(input("Enter the number to find PrimeFactors\n"))
    min_divisor = 2
    find_prime(value,min_divisor)
    print(f"Prime Factors of {value} --> ", end="")
    for val in set_temp:
        print(val, end=" ")




def main():
    # task_1()
    # task_2()
    # task_3()
    # task_4
    # task_5()
    task_6()

if __name__ == "__main__":
    main()
