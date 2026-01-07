import math

eg_list = [1,2,3,4,5,6]
eg_sqr_list = list(map((lambda x: int(math.pow(x,2))),eg_list))
print(eg_list)
print(eg_sqr_list)



# PRINTING SUBSTRING OF 3 LENGTHS
str_val = "EXAMPLE"
subsize = 3
for i in range(len(str_val)-subsize+1): # SUBSTRINGS OF 3 LENGTHS
    for j in range(i,(i+subsize)):
        print(str_val[j],end="")
    print()