#! /usr/bin/env python3

#set the name of input DNA sequence file
filename = 'dna.txt'

# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

#print(infile) 

# read the file
dna_sequence = infile.read().rstrip()

#print the dna_sequence
print(dna_sequence)

#close the file
infile.close()

#Frequency of A
dna_count_A = dna_sequence.count("A")
dna_fraction_A = dna_count_A / len(dna_sequence)
print("Freq of A: ","%.3f" % dna_fraction_A)

#Frequency of C
dna_count_C = dna_sequence.count("C")
dna_fraction_C = dna_count_C / len(dna_sequence)
print("Freq of C: ","%.3f" % dna_fraction_C)

#Frequency of G
dna_count_G = dna_sequence.count("G")
dna_fraction_G = dna_count_G / len(dna_sequence)
print("Freq of G: ","%.3f" % dna_fraction_G)

#Frequency of T
dna_count_T = dna_sequence.count("T")
dna_fraction_T = dna_count_T / len(dna_sequence)
print("Freq of T: ","%.3f" % dna_fraction_T)

#G+C content
GCcontent = dna_fraction_G + dna_fraction_C
print("G+C content: ", "%.3f" % GCcontent)

#check inside your script to make sure that your frequencies sum to 1
frequency = dna_fraction_G + dna_fraction_C + dna_fraction_A + dna_fraction_T
print(frequency)
