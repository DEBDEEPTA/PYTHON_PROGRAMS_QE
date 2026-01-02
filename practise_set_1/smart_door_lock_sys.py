
def locker(pin):

    for i in range(3):
        attempt_val = int(input(f"Attempt {i+1} -> "))
        if attempt_check(pin,attempt_val):
            print("ACESS GRANTED")
            return

    print("LOCKED")

def attempt_check(pin,attempt):
    if pin == attempt:
        return True
    return False

if __name__=="__main__":

    pin_val = int(input("Enter your pin\n"))
    locker(pin_val)