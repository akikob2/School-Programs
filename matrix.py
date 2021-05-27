# create the two dimensional matrix m
# 4 rows, 5 columns, 1 through 20

def sumRows(matrix):

    numRows = len(matrix)
    numCols = len(matrix[0])

    sums = []

    for row in range(numRows):
        rowSum = sum(matrix[row])
        sums.append(rowSum)

    return sums


def sumCols(matrix):

    numRows = len(matrix)
    numCols = len(matrix[0])

    sums = [0] * numCols

    for row in range(numRows):
        for col in range(numCols):
            sums[col] +=  matrix[row][col]

    return sums


def prettyPrint(matrix):

    numRows = len(matrix)
    numCols = len(matrix[0])

    for row in range(numRows):
        for col in range(numCols):
            print(format(matrix[row][col],"5d"),end ="")
        print("")

def main():

    m = []
    counter = 1

    for row in range(4):
        r = []
        for col in range(5):
            r.append(counter)
            counter += 1
        m.append(r)

    prettyPrint(m)

    print("Sum of Rows:", sumRows(m))
    print("Sum of cols:",sumCols(m))

main()
