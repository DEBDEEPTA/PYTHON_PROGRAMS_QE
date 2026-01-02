def over_flow(flow_list):

    capacity = 1000
    min_counter = 0

    for val in flow_list:
        capacity -= int(val)
        min_counter += 1
        if(capacity<0):
            return  min_counter

    return "NO OVER FLOW"



if __name__=="__main__":
    n = int(input())
    flow_vals = input()
    flow_val_list = flow_vals.split()

    print(over_flow(flow_val_list))
