#  File: MagicSquares.py
#  Description: Making a magic square given the length of a side
#  Student's Name: Akiko Barreras
#  Student's UT EID: ab63527
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 4/21/2020
#  Date Last Modified: 4/22/2020

class MagicSquare():

    def __init__(self,side):

        self.n = side #The sidelength of the square
        self.grid = []

        # Making a grid of sidelength by sidelength of all 0s
        
        for row in range(self.n):
            r = []
            for col in range(self.n):
                r.append(0)
            self.grid.append(r)

        #Putting numbers into the empty grid

        i = 1
        sizeGrid = (self.n)**2
        currentCol = int((self.n)/2)
        currentRow = 0

        while i != (sizeGrid+1):
            
            self.grid[currentRow][currentCol] = i

            # if i is a multiple of n
            if (i % self.n) == 0 and i != 1:
                currentRow += 1

            #if the number reaches the top row
            elif currentRow == 0:
                currentRow = self.n -  1
                currentCol += 1

            #if the number reaches the last column
            elif currentCol == self.n - 1:
                currentCol = 0
                currentRow -= 1

            else:
                currentRow -=1
                currentCol += 1

            i += 1

                  
    def display(self):

        numRows = len(self.grid)
        numCols = len(self.grid[0])

        for row in range(numRows):
            for col in range(numCols):
                print(format(self.grid[row][col],"5d"),end="")
            print("")


def main():

    #Loop that runs through the seven magic numbers

    for i in range(1,14,2):
        print("Magic Square of size",i)
        print("")
        print(MagicSquare(i).display())
        print("")

main()
    
        
