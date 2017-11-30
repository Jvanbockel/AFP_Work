line = []
#Opens the input file
file = open("dna_Sequence")
#Opens the output file
file2 = open("Trimmed_DNA","w+")

#Creates loop to edit each line within the file
for line in file:
    #Cuts out the first 14 characters
    sequence = line[14:]
    #Writes new sequences to a new file
    file2.write(sequence)
    #Displays the length of each new DNA sequence
    print("Processed sequence with length",len(sequence))




