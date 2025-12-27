"""
    1. Gambler.
        a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
                    he/she goes broke (i.e. has no money) or reach $goal.
                    Keeps track of the number of times he/she wins and the number of bets he/she makes.
                    Run the experiment N times, averages the results, and prints them out.
        b. I/P -> $Stake, $Goal and Number of times
        c. Logic -> Play till the gambler is broke or has won
        d. O/P -> Print Number of Wins and Percentage of Win and Loss.
"""
import random


def gambler(stake,goal,times):
    win =  0
    loss = 0
    bets = 0
    for _ in range(times):
        money = stake
        while (money<goal and money>0 ):
            bets += 1
            random_value = random.randint(0,1)
            if(random_value == 0):
                money -= 1
            else:
                money += 1

        if(money == goal):
            win += 1
        else:
            loss += 1

    print(f"TOTAL WINS -> {win}")
    win_ratio = (win/times)*100
    loss_ratio = (loss/times)*100
    print(f"Win percentage -> {win_ratio}")
    print(f"loss percentage -> {loss_ratio}")


def main():
    stake = int(input("Enter stake amount in $\n"))
    goal = int(input("Enter goal amount in $\n"))
    times = int(input("Enter number of times to put bet\n"))
    gambler(stake,goal,times)

if __name__ == "__main__":
    main()