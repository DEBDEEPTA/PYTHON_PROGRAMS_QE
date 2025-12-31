import math


def prime_count(start,end):
    count = 0
    for i in range(start,end+1):
        if(is_prime(i)):
            count += 1

    return  count

def is_prime(value):
    end = int(math.sqrt(value))
    for i in range(2,end+1):
            if(value%i == 0):
                return False
    return True





if __name__ == "__main__":
    start = int(input())
    end = int(input())
    print(prime_count(start,end))
