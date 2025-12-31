def num_count(nums):
    count = 0
    while(nums % 2 == 0):
        count += 1
        nums = nums//2

    return count


if __name__=="__main__":
    nums = int(input())
    print(num_count(nums))