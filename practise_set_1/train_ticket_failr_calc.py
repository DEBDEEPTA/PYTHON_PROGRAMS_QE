
def fare_calc(d,a):
    fare = d * 2
    if(a >=60):
        fare -= (fare*0.3) # 30% DISSCOUNT
    elif(a<12):
        fare -= (fare*0.5) # 50% DISSCOUNT
    return fare

if __name__=="__main__":
    distance = int(input())
    age = int(input())

    print(fare_calc(distance,age))