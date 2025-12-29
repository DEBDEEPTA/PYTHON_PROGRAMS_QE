from enum import Flag


def transaction_validator(bal,ammount_list):
     # CHECK TRANSACTION VALUE MULTIPLE OF 100
     for amnt in ammount_list:
         if(amnt%100 == 0):
             if((bal - amnt) >=0):
                 bal -= amnt
                 print("SUCCESS")
             else:
                 print("FAILED")

         else:
             print("FAILED")

     print(bal)

if __name__ == "__main__":

    initial_bal = int(input("Enter Initial Bal\n"))
    withdrawl_num = int(input("Enter number of With draws\n"))

    ammount_list = [int(input(f"Enter Withdraw No.{i+1} -> ")) for i in range(withdrawl_num)]

    transaction_validator(initial_bal,ammount_list)