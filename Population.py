#  Description: Using dictionaries to tally up the 1st digit of populations

def main():

    census = open("2009CensusData.txt","r")

    #Making an empty dictionary
    freqDis = {}
    for i in range(1,10):
        freqDis[str(i)] = 0

    #Making the heading
    print(format("Digit","8s"),end="")
    print(format("Count","10s"),end="")
    print("%")
    print("-" * 21)

    #Going through the text file line by line and making the dictionary
    line = census.readline() #first line, need to ignore
    line = census.readline()
    total = 0

    while line != "":

        #Splitting up the line
        stateStats = line.split()
        pop = stateStats[-1]

        #Figuring out what the number starts with and adding to dictionary
        for j in range(1,10):
            if str(j) == pop[0]:
                freqDis[str(j)] += 1
                total += 1
            else:
                continue
            
        line = census.readline()
        
    #Putting info into the table
    for num in range(1,10):
        print(format(num,"<8d"),end="")
        print(format(freqDis[str(num)],">5d"),end="")
        frequency = 100 * ((freqDis[str(num)]) / total)
        print(format(frequency,">8.1f"))

    print()

main()

        
                

        
                
        
                
            
        
        
        
        
    
