# Write a function called dateConvert() that takes as an argument a
# string representing a date in the form "MM/DD/YYY" and returns a
# string representing the long form of the date, such as 'April 16, 2020

def dateConvert(dateString): #input is 04/16/2020

    monthWords = ["January","February","March","April","May","June",
                  "July","August","September","October","November",
                  "December"]

    month,day,year = dateString.split("/")
        #get a list, but then assign them to 3 variables

    monthWord = monthWords[int(month)-1]


    return monthWord + " " + day + ", " + year

def main():

    myDate = input("Enter a date in the form MM/DD/YYYY: ")

    while myDate!= "":
        print(dateConvert(myDate))
        myDate = input("Enter a date in the form MM/DD/YYYY: ")

main()
