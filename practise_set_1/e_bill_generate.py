def e_calc(units):
    usage = units
    charge = 0
    if units -100 > 0:
        charge += (100*3)
        units -= 100
    else:
        charge += (100*3)
        return charge

    if units -100 > 0:
        charge += (100*5)
        units -= 100
    else:
        charge += (100*5)
        return charge

    if units > 0:
        charge += (units*8)

    if usage > 300:
        charge += ((units*10)/100)

    return  charge


if __name__=="__main__":
    units_val = int(input("Enter Units\n"))
    print(e_calc(units_val)