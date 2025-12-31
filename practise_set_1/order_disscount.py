
def calc(ammount):
    temp_ammount = ammount
    if (ammount >= 5000):
        temp_ammount -= (temp_ammount * 0.2)
        return  temp_ammount
    if (ammount >= 3000):
        temp_ammount -= (temp_ammount * 0.1)
        return  temp_ammount
    if (ammount >= 1000):
        temp_ammount -= (temp_ammount * 0.05)
        return  temp_ammount

    return ammount


if __name__ == "__main__":
    ammount = int(input())
    print(calc(ammount))





