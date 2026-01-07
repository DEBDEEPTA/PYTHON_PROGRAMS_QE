def two_vals(key,nums_list):
    temp_list = []
    for i in range(len(nums_list)):
        for j in range(i+1,len(nums_list)):
            if(nums_list[i]+nums_list[j] == key):
                temp_list.append(i)
                temp_list.append(j)
                return  temp_list

    return None

if __name__=="__main__":

    num_list = [1,5,4,3,3]
    target = 6
    print(two_vals(target,num_list))
