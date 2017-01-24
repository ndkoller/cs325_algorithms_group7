# Import functions
from datetime import datetime
from random import *


# File names
data_file = 'MSS_Problems.txt'
results_file = 'MSS_Results1.txt'
exp_results_file = 'MS_ExperimentalResults1.txt'


# Algorithm 1: Enumeration
def MAXSUBARRAY_Enum(array):
    n = len(array)
    max_sum = -1
    max_i = 0
    max_j = 0
    for i in range(n):
        for j in range(i, n):
            sa_sum = 0
            for ea in array[i:j+1]:
                sa_sum += int(ea)
            if sa_sum > max_sum:
                max_sum = sa_sum
                max_i = i
                max_j = j
    return array[max_i:max_j+1], max_sum


# Algorithm 2: Better Enumeration
def MAXSUBARRAY_BetterEnum(array):
    n = len(array)
    max_sum = -1
    max_i = 0
    max_j = 0
    for i in range(n):
        sa_sum = 0
        for j in range(i, n):
            sa_sum += int(array[j])
            if sa_sum > max_sum:
                max_sum = sa_sum
                max_i = i
                max_j = j
    return array[max_i:max_j+1], max_sum


# Common code to write results to output file
def WRITERESULTS(data, subarray, maxsum, fileobject):
    for ea in data:
        fileobject.write(str(ea) + " ")
    fileobject.write("\n")
    for ea in subarray:
        fileobject.write(str(ea) + " ")
    fileobject.write("\n")
    fileobject.write(str(maxsum) + "\n\n")


# Common code to time the algorithms
def RUNEXPERIMENT(alg, n_array, n_multiplier, output_file):
    with open(output_file, 'a') as fw:
        fw.write("N Values\tTime (Seconds)\n")

    for ea in n_array:
        # Create array of random integers of size N
        array = []
        n_adjusted = int(ea) * n_multiplier
        for i in range(n_adjusted):
            array.append(randint(-100, 101))

        # Start timer
        startTime = datetime.now()

        # Run Algorithm
        subarray, maxsum = alg(array)

        # stop timer
        totalTime = datetime.now() - startTime

        with open(output_file, 'a') as fw:
            fw.write(str(n_adjusted) + "\t" + str(totalTime.total_seconds()) + "\n")
        print("N =", n_adjusted, "| Time =", totalTime.total_seconds())


######## Run Algorithms on Input File ########

# Delete contents of test results file
with open(results_file, 'w') as fw:
    fw.write("")


# Open data_file
with open(data_file, 'r') as fr:

    # Read each line
    for line in fr:

        # Split line into an array of values
        data = line.split()

        # Append Enumeration results to 'results_file'
        with open(results_file, 'a') as fw:

            # Call Algorithm 1: Enumeration to get the max sub array and max sum
            subarray, maxsum = MAXSUBARRAY_Enum(data)

            fw.write("Algorithm 1: Enumeration Results\n")
            WRITERESULTS(data, subarray, maxsum, fw)

            # Call Algorithm 2: Enumeration to get the max sub array and max sum
            subarray, maxsum = MAXSUBARRAY_BetterEnum(data)

            fw.write("Algorithm 2: Better Enumeration Results\n")
            WRITERESULTS(data, subarray, maxsum, fw)


######## Experimental Time Runs ########

# Delete contents of test results file
with open(exp_results_file, 'w') as fw:
    fw.write("Experimental Time Runs\n")
print("Experimental Time Runs")

# Array for N sizes
N = [25, 35, 50, 75, 100, 125, 250, 500, 750, 1000]

# Algorithm 1: Enumeration
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 1: Enumeration\n")
print("\nAlgorithm 1: Enumeration")

RUNEXPERIMENT(MAXSUBARRAY_Enum, N, 1, exp_results_file)

# Algorithm 2: Better Enumeration
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 2: Better Enumeration\n")
print("\nAlgorithm 2: Better Enumeration")

RUNEXPERIMENT(MAXSUBARRAY_BetterEnum, N, 10, exp_results_file)