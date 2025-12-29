import  random
def cupon_generator(num_list):
    print(num_list)

   # AMBIGUITY IN UNDERSTANDING PROBLEM STATEMENT

def main():
   n = int(input("Enter number of elements\n"))

   num_list = [ int(input(f"Enter Element {i+1} -> ")) for i in range(n)]

   cupon_generator(num_list)

if __name__=="__main__":
    main()