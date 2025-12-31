import math

def bin_2_dec(bin_num):

    rev_bin_num = reversed(bin_num)
    dec_num = 0
    power = 0
    for char in rev_bin_num:
        if(char == "1"):
            dec_num += math.pow(2,power)
        power += 1

    return dec_num


def main():
    bin_num = input("Enter binary Number\n")
    print(bin_2_dec(bin_num))

if __name__ == "__main__":
    main()