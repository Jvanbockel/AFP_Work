#The sequence that we will be finding the amount of G's and C's from
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#Tells the user what is happening
print("This program will display te GC content of a DNA sequence")

#Allows user to enter their own sequence
mySequence = input("Enter your DNA sequence: ")

#Finds the total amount letters in the sequence
total = len(mySequence)

#Finds how many G's are in the sequecne
g = mySequence.count("G")

#Finds how many C's are in the sequecne
c = mySequence.count("C")

#Adds the G's and C's together
gc = g + c

#Divides added G's and C's by the total amount of letters
gc = gc / total

#Moves the decimal point forward to give a whole number
percent = gc * 100

#Format method allows me to format the float with any number of decimal
#places. I can easily add more placeholders and variables
print("The GC content of the sequence is {0:.2f}%".format(percent))

#Prints the percentage of G's and C's and rounds it to the 2nd decimal place
print(str(round(percent, 2))+"%")