#! /usr/bin/env python3

#This script generates a PBS file for the AHPCC Razor cluster

# define some variables
job_name = "rbmahbubtestpinnacle" 
queue = "comp01"
prefix = job_name
number_of_nodes = 1
number_of_processors = 1
wall = 1 #this is in hours

# This section prints the header/required info for the PBS script
print("#SBATCH -J", job_name) # job name
print("#SBATCH --partition", queue)  # which queue to use
print("#SBATCH -oe") #join the STDOUT and STDERR into a single file
print("#SBATCH --nodes=" + str(number_of_nodes)) # how many nodes
print("#SBATCH --ntasks-per-node=" + str(number_of_processors)) #how many processors
print("#SBATCH --time=" + str(wall)) # set the walltime (default to 1 hr)

print("export OMP_NUM_THREADS=32")
 
# load required modules
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
 
# cd into the directory where you're submitting this script from
print("cd $SLURM_SUBMIT_DIR")

# copy files from storage to scratch
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')

# cd onto the scratch disk to run the job
print("cd /scratch/$SLURM_JOB_ID/")

# run the Trinity assembly
print("/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2")
 
# copy output files back to storage
print("rsync -av trinity_Run2 $SLURM_SUBMIT_DIR")

