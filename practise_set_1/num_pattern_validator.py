

def num_validator(num):
    temp_str = str(num)

    for i in range(len(temp_str)-1):
        cur_val = int(temp_str[i])
        next_val = int(temp_str[i+1])
        if(cur_val<next_val):
            continue
        else:
            return False

    return True


if __name__=="__main__":
    num_val = int(input())
    if num_validator(num_val):
        print("YES")
    else:
        print("NO")