

def miss_sequence_num_finder(nums_list):

    nums_list.sort()
    print(num_list)
    for i in range(len(nums_list)):
        cur_val = nums_list[i]+1
        next_val = nums_list[i+1]
        if not(cur_val == next_val):
            return cur_val
        else:
            continue

    return None



if __name__=="__main__":
    num_list = [2, 1, 4, 6, 5,3,8]

    # print(miss_sequence_num_finder(num_list))



