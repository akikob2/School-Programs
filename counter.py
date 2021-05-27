#   Write a program that:
# - reads a list of integers and counts how many 1s, 2s, 3s, ... 100s
#   are entered
# - print out "The number of 1s:" followed by a count
# - "The number of 2s:" followed by a count, up to the 100s
# - one line each but do NOT print anything that has a count of 0s

def main():

    counters = 100* [0]
    #makes a list of 100 0's
    
    value = input("Enter a number: ")

    while value != "":
        counters[int(value) - 1] += 1
        value = input("Enter a number: ")

    for i in range(1,101):
        if counters[i-1] != 0:
            print("The number of",str(i)+"'s:",counters[i-1])

main()

        
