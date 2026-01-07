def dublicate_num_finder(nums_list):
    dublicate_num_set = set()
    for i in nums_list:
        if frequency(i,nums_list) > 1:
            dublicate_num_set.add(i)

    print(dublicate_num_set)

def frequency(val,nums):
    count_val = 0
    for i in nums:
        if(i == val):
            count_val += 1
    return  count_val

if __name__=="__main__":
    num_list = [1,2,3,6,1,7,2,5,6,7]
    dublicate_num_finder(num_list)