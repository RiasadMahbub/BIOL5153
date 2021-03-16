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
print('#PBS -N', job_name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') #join the STDOUT and STDERR into a single file
print('#PBS -o', job_name, '.$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(number_of_nodes)+':ppn='+str(number_of_processors)) # how many resource to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

#load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# commands for this job
print('# insert commands here')

