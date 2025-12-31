import re
from itertools import count


def vowel_freq(str_val):
    count = 0
    for char in str_val:
        if(re.match("[aeiouAEIOU]",char)):
            count += 1

    return count


if __name__=="__main__":
    str_val = input()
    print(vowel_freq(str_val))