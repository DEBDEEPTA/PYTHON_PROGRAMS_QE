

"""
         1=>  T >= 30   : R
         31=>  T >=45   : Y
         46=>  T >=90   : G

         if( T > 90)

"""

time = int(input("Enter Time -> "))

if(time > 90):
    time = time%90
    if (1 <= time <= 30):
        print("RED")
    elif (31 <= time <= 45):
        print("YELLOW")
    elif (46 <= time <= 90) or time == 0:
        print("GREEN")

else:
    if (1 <= time <= 30):
        print("RED")
    elif (31 <= time <= 45):
        print("YELLOW")
    elif (46 <= time <= 90):
        print("GREEN")


