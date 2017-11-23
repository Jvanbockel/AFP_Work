sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
#Code finds the specific section where the combinatin=on of 'GAATTC' is and give an index position back
#It is then added by one due to the indexes starting at 0
section1 = sequence.find("GAATTC") + 1
#Uses basic maths to find the length of the second fragment by subtracting it by tht total amount.
section2 = len(sequence) - section1
#Displays the length of eac fragment in a short sentance
print("The length of the first fragment is", section1,"and the length of the second fragment is",str(section2)+".")