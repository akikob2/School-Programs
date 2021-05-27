#  Description: Getting the number of combinations for 0 to 52 cards

def main():

    #making factorial function
    def factorial(num):
        fact = 1
        for i in range (1,num+1):
            fact *= i
        return fact

    #combination function
    def combinations(n,r):
        x = factorial(n)
        y = factorial(r)
        z = factorial(n-r)
        integer = x // (y*z)
        return integer

    #header
    print()
    print("Cards",end='')
    print(format("Combinations",">17s"))
    print("="*22)

    #printing numbers of cards and their combinations
    for i in range(0,53):
        print(format(i,">3d"),end="")
        print(format(combinations(52,i),">19d"))
    print()


main()
