# Import functions
from datetime import datetime
from random import *
import p2algorithms as algs
from itertools import zip_longest
import sys

# File names
if len(sys.argv) == 1:
    data_file = 'coins.txt'         # for testing purposes
else:
    data_file = str(sys.argv[1])
results_file = data_file[:-4] + 'change.txt'
exp_results_file = data_file[:-4] + '_ExperimentalResults.txt'

# Python Documentation Recipe to group file input
def GROUPER(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


# Common code to write results to output file
def WRITERESULTS(data, coincounts, totalcoins, fileobject):
    for ea in data:
        fileobject.write(str(ea) + "\t")
    fileobject.write("\n")
    for ea in coincounts:
        fileobject.write(str(ea) + "\t")
    fileobject.write("\n")
    fileobject.write(str(totalcoins) + "\n\n")


# Common code to time the algorithms
def RUNEXPERIMENT(alg, n_array, data, target, n_multiplier, output_file):
    with open(output_file, 'a') as fw:
        fw.write("N Values\tTime (Seconds)\n")

    '''
    Update below needs updating for Project 2 (left over from Project 1)
    for ea in n_array:
        # Create array of random integers of size N
        array = []
        n_adjusted = int(ea) * n_multiplier
        for i in range(n_adjusted):
            array.append(randint(-100, 101))

        # Start timer
        startTime = datetime.now()

        # Run Algorithm
        c, m = alg(data, target)

        # stop timer
        totalTime = datetime.now() - startTime

        with open(output_file, 'a') as fw:
            fw.write(str(n_adjusted) + "\t" + str(totalTime.total_seconds()) + "\n")
        print("N =", n_adjusted, "| Time =", totalTime.total_seconds(), "s")
    '''

######## Run Algorithms on Input File ########

# Delete contents of test results file
with open(results_file, 'w') as fw:
    fw.write("")

# Open data_file
with open(data_file, 'r') as fr:
    
    # Read every 2 lines using grouper function
    for line1, line2 in GROUPER(fr,2):

        # Split line into an array of values 
        # This is the denomination array in test files
        data = list(map(int, line1.split()))
        dataTarget = int(line2)
        
        # Append Enumeration results to 'results_file'
        with open(results_file, 'a') as fw:

            # Call Algorithm 1: ChangeSlow to get the max sub array and max sum
            c, m = algs.ChangeSlow(data, dataTarget)
            print("Algorithm 1: Change Slow\nc:", c, 'm:', m)

            fw.write("Algorithm 1: Change Slow\n")
            WRITERESULTS(data, c, m, fw)

            # Call Algorithm 2: ChangeGreedy
            c, m = algs.ChangeGreedy(data, dataTarget)
            print("Algorithm 2: Change Greedy\nc:", c, 'm:', m)

            fw.write("Algorithm 2: Change Greedy\n")
            WRITERESULTS(data, c, m, fw)


######## Experimental Time Runs ########

# Delete contents of test results file
with open(exp_results_file, 'w') as fw:
    fw.write("Experimental Time Runs\n")
print("Experimental Time Runs")

# Array for N sizes
N = []
i = 2010
for i in range(2010, 2205, 5):
    N.append(i)
# print("N:", N)    # for reference only, checking what N is

''' Code below needs updating for Project 2 (left over from Project 1)'''
# Algorithm 1: Enumeration
# with open(exp_results_file, 'a') as fw:
# fw.write("\nAlgorithm 1: Enumeration\n")
# print("\nAlgorithm 1: Enumeration")

# RUNEXPERIMENT(algs.MAXSUBARRAY_Enum, N, 1, exp_results_file)
