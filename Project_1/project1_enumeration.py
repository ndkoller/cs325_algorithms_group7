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

            for ea in data:
                fw.write(str(ea) + " ")
            fw.write("\n")
            for ea in subarray:
                fw.write(str(ea) + " ")
            fw.write("\n")
            fw.write(str(maxsum) + "\n\n")

            fw.write("Algorithm 2: Better Enumeration Results\n")

            # Call Algorithm 2: Enumeration to get the max sub array and max sum
            subarray, maxsum = MAXSUBARRAY_BetterEnum(data)

            for ea in data:
                fw.write(str(ea) + " ")
            fw.write("\n")
            for ea in subarray:
                fw.write(str(ea) + " ")
            fw.write("\n")
            fw.write(str(maxsum) + "\n\n")

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

for ea in N:
    # Create array of random integers of size N
    array = []
    n_multiplier = 1
    N_adjusted = int(ea) * n_multiplier
    for i in range(N_adjusted):
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


# Algorithm 2: Better Enumeration
with open(exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 2: Better Enumeration\n")
print("\nAlgorithm 2: Better Enumeration")

for ea in N:
    # Create array of random integers of size N
    array = []
    n_multiplier = 10
    N_adjusted = int(ea) * n_multiplier
    for i in range(N_adjusted):
        array.append(randint(-100, 101))

    # Start timer
    startTime = datetime.now()

    # Call Algorithm 1: Enumeration to get the max sub array and max sum
    subarray, maxsum = MAXSUBARRAY_BetterEnum(array)

    # stop timer
    totalTime = datetime.now() - startTime

    with open(exp_results_file, 'a') as fw:
        fw.write("N = " + str(N_adjusted) + " | Time = " + str(totalTime.total_seconds()) + "\n")
    print("N =", N_adjusted, "| Time =", totalTime.total_seconds())
