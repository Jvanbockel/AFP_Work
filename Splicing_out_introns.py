sequence= "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCG" \
          "ATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGA" \
          "TGCATCGACTACTAT"
#Finds exons and introns within the sequence
exon1 = sequence[0:63]
exon2 = sequence[91:200]
intron = sequence[64:90]
#Displays the sequence with the intron cut out of it
print(exon1+exon2)
#Finds the length of both exons as an int
code = len(exon1) + len(exon2)
#Converts into percentage
percent = code / len(sequence)
percent = percent * 100
#Displays percentage
print(str(round(percent,2))+"%")
#Displays sequence with the intron in lower case
print(exon1+intron.lower()+exon2)

