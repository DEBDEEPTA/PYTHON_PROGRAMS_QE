def rev_num(num):
    str_num = str(num)
    rev_str_num = str_num[::-1]
    rev_num = int(rev_str_num)
    print(rev_num)
    #print(type(rev_num)) # FOR CHECKING


if __name__ =="__main__":
    input_num = int(input("Enter A Integer\n"))
    rev_num(input_num)


