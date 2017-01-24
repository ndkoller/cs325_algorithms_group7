# Import functions
from datetime import datetime
from random import *


# File names
data_file = 'MSS_Problems.txt'
results_file = 'MSS_TestResults1.txt'
exp_results_file = 'MS_ExperimentalResults.txt'


# Algorithm 1: Enumeration
def MAXSUBARRAY_Enum(array):
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


# Delete contents of test results file
with open(results_file, 'w') as fw:
    fw.write("Algorithm 1: Enumeration Experimental Run Times\n")

print("Algorithm 1: Enumeration Experimental Run Times")


# Open data_file
with open(data_file, 'r') as fr:

    # Read each line
    for line in fr:

        # Split line into an array of values
        data = line.split()

        # Call Algorithm 1: Enumeration to get the max sub array and max sum
        subarray, maxsum = MAXSUBARRAY_Enum(data)

        # Append results to 'results_file'
        with open(results_file, 'a') as fw:
            for ea in data:
                fw.write(str(ea) + " ")
            fw.write("\n")
            for ea in subarray:
                fw.write(str(ea) + " ")
            fw.write("\n")
            fw.write(str(maxsum) + "\n\n")


# Experimental Analysis

# Delete contents of test results file
with open(exp_results_file, 'w') as fw:
    fw.write("")

# Array for N sizes
N = [100, 250, 500, 1000, 2500, 5000, 10000]

for ea in N:
    # Create array of random integers of size N
    array = []
    for i in range(ea):
        array.append(randint(-100, 101))

    # Start timer
    startTime = datetime.now()

    # Call Algorithm 1: Enumeration to get the max sub array and max sum
    subarray, maxsum = MAXSUBARRAY_Enum(array)

    # stop timer
    totalTime = datetime.now() - startTime

    with open(exp_results_file, 'a') as fw:
        fw.write("N = " + str(ea) + " | Time = " + str(totalTime.total_seconds()) + "\n")
    print("N =", ea, "| Time =", totalTime.total_seconds())
