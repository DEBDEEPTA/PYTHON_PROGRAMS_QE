
def b_drain(min):

    count = 0
    b_capacity = 100
    while(b_capacity >=0):
        b_capacity -= min
        count += 1
    return  count


if __name__ == "__main__":
    d_min = int(input())
    print(b_drain(d_min))