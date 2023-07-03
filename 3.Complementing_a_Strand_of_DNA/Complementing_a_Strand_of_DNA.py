# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s
#  is the string sc
#  formed by reversing the symbols of s
# , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s
#  of length at most 1000 bp.

# Return: The reverse complement sc
#  of s
# .

# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

fn = "rosalind_revc.txt"
with open(fn,'r') as f :
    DNA = f.readline().replace("\n", "")
    complement = {"A" : "T", "C" : "G", "T" : "A", "G" : "C"}
    RVDNA = ""
    for base in DNA:
        RVDNA = complement[base] + RVDNA

    print(RVDNA)