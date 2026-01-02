import math


def arm_strong_check(num):
    temp_str =str(num)
    generated_num = 0
    for chr in temp_str:
        digit_val = int(chr)
        generated_num += math.pow(digit_val,3)

    if(num == generated_num):
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    num_val = int(input())
    arm_strong_check(num_val)