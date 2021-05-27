#  Description: Pretending to be a teacher and making a grade book

def main():

    gradeFile = open("gradeInput.txt","r") #This was a textfile given to us
    outFile = open("gradeOutput.txt","w")

    #Writing the heading
    outFile.write(format(" "*30))
    outFile.write(format("HW","7s"))
    outFile.write(format("Exam","7s"))
    outFile.write("Final" + "\n")
    outFile.write(format("Last Name","15s"))
    outFile.write(format("First Name","15s"))
    outFile.write(format("Avg","7s"))
    outFile.write(format("Avg","7s"))
    outFile.write("Grade" + "\n")
    outFile.write("-" * 49 + "\n")  

    #Going through the text file line by line
    line = gradeFile.readline()

    while line != "":

        #Splitting the line into names and grades
        studentStats = line.split()
        studentName = studentStats[0].split(",")
        lastName = studentName[0]
        firstName = studentName[1]

        #Getting a list of only the grades
        studentStats.remove(studentStats[0])

        hw = []
        exam = []
        for i in range(0,len(studentStats)-3):
            hw.append(int(studentStats[i]))
        for i in range(15,18):
            exam.append(int(studentStats[i]))

        #getting Averages and final grade
        hwAvg = (sum(hw))/len(hw)
        examAvg = (sum(exam))/len(exam)
        final = (.55 * hwAvg) + (.45 * examAvg)

        #Putting it into the file
        outFile.write(format(lastName,"15s"))
        outFile.write(format(firstName,"15s"))
        outFile.write(format(format(hwAvg,"3.1f"),"7s"))
        outFile.write(format(format(examAvg,"3.1f"),"7s"))
        outFile.write(format(format(final,"3.1f"),"7s"))
        outFile.write("\n")

        line = gradeFile.readline()

    gradeFile.close()
    outFile.close()        

main()
