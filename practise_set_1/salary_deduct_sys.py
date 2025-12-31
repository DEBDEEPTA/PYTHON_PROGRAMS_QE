def cal_sal(basic,l_days,a_days):
    if(l_days>10):
        basic -= (basic*0.1)
    if(l_days>5):               # AS CUMULATIVE (elif not USED)
        basic -= (basic*0.05)

    if(a_days > 2):
        basic -= (basic*0.05)

    return int(basic)

def main():
    basic = int(input())
    l_days= int(input())
    a_days = int(input())


    print(cal_sal(basic,l_days,a_days))


if __name__=="__main__":
    main()