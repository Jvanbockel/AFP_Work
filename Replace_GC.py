sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Replaces all A's and T's with G's and C's respectively
newSequence = sequence.replace("T","a").replace("G","c").replace("A","t").replace("C","g")

#Displays inverse sequence
print(newSequence.upper())
