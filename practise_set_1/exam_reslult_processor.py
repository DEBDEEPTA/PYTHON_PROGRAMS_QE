
def res_calc(marks):
    if any( m<35 for m in marks):
        print("FAIL")


    elif (sum(marks)/len(marks) >= 75):
        print("DISTINCTION")

    else:
        print("PASS")
if __name__ == "__main__":

     result_list = [int(input(f"Enter m{i+1} ->")) for i in range(5)]

     res_calc(result_list)