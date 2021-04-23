#! /Users/riasadbinmahbub/opt/anaconda3/bin/python3

#import the required modules
import csv
import argparse
from Bio import SeqIO
import re
from collections import defaultdict 

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

#create an argument parser object
parser = argparse.ArgumentParser(description= 'To determine how genes with exons and introns are encoded.')

# add positional arguments
parser.add_argument("gff", help = 'name of the GFF file')
parser.add_argument("fasta", help = 'name of the FASTA file')
parser.add_argument("gene_name", help = "name of the gene to extract")
parser.add_argument("feature_type", help = 'type of feature to extract')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(genome.seq)


# Add a function calledrev_compto yourparseGFF.pyscript that will calculate and return the reversecomplement of features that are on the ‘-’ strand. 
def rev_comp(genome_seq, strand):
	if strand == '-':
		return(print(genome_seq).reverse_complement()
	else:
		return(print(genome_seq))

#open and read in GFF file
with open(args.gff, 'r') as gff_in:

    #create a csv reader object
    reader = csv.reader(gff_in, delimiter ='\t')

    #loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        #skip comment line
        if(not line):
            continue
        #skip blank lines
        elif(re.search('^#', line[0])):
            continue

        # else its a data line    
        else :
            feature = line[2]
            species = line[0] 
            start = line[3]
            end = line[4]
            strand = line[6] 
            attributes = line[8] 
            exon = re.search(r"exon(\d)", attributes) 

            if (feature_type == args.feature_type_arg):
            
        
