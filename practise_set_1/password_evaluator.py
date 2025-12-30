
def pass_eval(password):
    flag = False
    if(any(ch.isdigit() for ch in password)):
        if(any(ch.isupper() for ch in password)):
            if(len(password)>=8):
                flag = True

    if(flag):
        print("STRONG")
    else:
        print("WEAK")


if __name__ == "__main__":
    password  = input("Enter Password\n")

    pass_eval(password)



