line = []
file = open("genomic_dna")

for line in file:
    sequence = line[:]
    print(sequence)