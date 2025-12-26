def triplet_sum():
    """
        2. Sum of three Integer adds to ZERO
            a. Desc -> A program with cubic running time. Read in N integers and counts the
                        number of triples that sum to exactly 0.
            b. I/P -> N number of integer, and N integer input array
            c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
            d. O/P -> One Output is number of distinct triplets as well as the second output is to
                      print the distinct triplets.
    """
    nums = int(input("eneter array size\n"))
    array = []
    for i in range(nums):
        val = int(input())
        array.append(val)

   # TEST
   # print(array)
    sub_size = 3
    count = 0
    for i in range(len(array)-sub_size+1):
        sum = 0
        for j in range(i,i+sub_size):
            # TEST
            #print(f"{array[j]} ",end=
            sum +=  array[j]
        #TEST
        #print()
        if(sum == 0):
            count += 1

    return count


def main():

    print("DISTINCT TRIPLATES FOUND ->",triplet_sum())

if __name__ == "__main__":
    main()