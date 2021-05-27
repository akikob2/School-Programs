#  Description: proving the Monty Hall problem

import random

def roll(n):
    x = random.randint(1,n)
    return x

def runOneTrial():
    prize = roll(3)
    guess = roll(3)
    view = roll(3)

    #making sure that view isn't the prize or guess number/door
    while view == prize or view == guess:
        view = roll(3)

    #making sure the newGuess isn't the previous quess or the view number/door
    newGuess = roll(3)
    while newGuess == guess or newGuess == view:
        newGuess = roll(3)
            
    if newGuess == prize:
        return "win",prize,guess,view,newGuess
    else:
        return "lose",prize,guess,view,newGuess
    

def main():
    
    num = int(input("How many trials do you want to run? "))

    print()
    print("Prize",end="  ")
    print("Guess",end="  ")
    print("View",end="  ")
    print("New Guess")

    winsSwitch = 0

    #running each trial

    for i in range(0,num):
        result,numP,numG,numV,numNG = runOneTrial()
        print(format(numP,"^5d"),end="")
        print(format(numG,"^9d"),end="")
        print(format(numV,"^5d"),end="")
        print(format(numNG,"^13d"))
        if result == "win":
            winsSwitch += 1
    print()
    probSwitch = winsSwitch/num
    probNotSwitch = 1 - probSwitch

    print("Probability of winning if you switch =",probSwitch)
    print("Probability of winning if you do not switch =",probNotSwitch)
    

main()
