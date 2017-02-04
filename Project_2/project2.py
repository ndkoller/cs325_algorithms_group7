# Import functions
from datetime import datetime
from random import *
import p2algorithms as algs
from itertools import zip_longest
import sys
import math

# File names
if len(sys.argv) == 1:
    data_file = 'correctnessTest.txt'         # for testing purposes
else:
    data_file = str(sys.argv[1])
results_file = data_file[:-4] + 'change.txt'
PR3_exp_results_file = 'PR3_ExperimentalResults.txt'

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
def RUNEXPERIMENT(alg, n_array, data, n_multiplier, output_file):
    with open(output_file, 'a') as fw:
        fw.write("N Values\tTime (Seconds)\n")

    # Update below needs updating for Project 2 (left over from Project 1)
    for ea in n_array:
        
        target = ea * n_multiplier
        
        # Start timer
        startTime = datetime.now()

        # Run Algorithm
        c, m = alg(data, target)

        # stop timer
        totalTime = datetime.now() - startTime

        with open(output_file, 'a') as fw:
            fw.write(str(target) + "\t" + str(totalTime.total_seconds()) + "s | Coin = " + str(m) + "\n")
        print("N =", target, "| Time =", totalTime.total_seconds(), "s | Coin = ", m)
    

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

            # Call Algorithm 3: ChangeDP
            c, m = algs.ChangeDP(data, dataTarget)
            print("Algorithm 3: Change DP\nc:", c, 'm:', m)

            fw.write("Algorithm 3: Change DP\n")
            WRITERESULTS(data, c, m, fw)


######## Experimental Time Runs ########

# Delete contents of test results file
with open(PR3_exp_results_file, 'w') as fw:
    fw.write("Experimental Time Runs\n")
print("Experimental Time Runs")

# Array for Project Report Question 3
N = []
i = 100
for i in range(100, 305, 5):
    N.append(i)
VN = [1, 5, 10, 25, 50]

# Alternative Arrays for Project Report Question 4
M = []
j = 2000
for j in range(2000, 2201, 1):
    M.append(j)
VM1 = [1, 2, 6, 12, 24, 48, 60]
VM2 = [1, 6, 13, 37, 150]
j = 10000
ML = []
for j in range(10000, 10101, 1):
    ML.append(j)
    
# Array for Project Report Question 5 (Re-Use M's from 4)
F = [1]
k = 2
for k in range(2, 32, 2):
    F.append(k)

# Question 7 Random Array Sizes Positive Sorted random values
        
# Create array of random integers of size N
# array = []
# n_adjusted = int(ea) * n_multiplier
# for i in range(n_adjusted):
    # array.append(randint(-100, 101))
   
''' Code below needs updating for Project 2 (left over from Project 1)'''
# Question 3 Experimental Run:
print("\n******Project Report Question 3******")

# Algorithm 1: Change Slow
with open(PR3_exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 1: Change Slow\n")
print("\nAlgorithm 1: Change Slow")

RUNEXPERIMENT(algs.ChangeSlow, N, VN, 1, PR3_exp_results_file)

# Algorithm 2: Change Greedy
with open(PR3_exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 2: Change Greedy\n")
print("\nAlgorithm 2: Change Greedy")

RUNEXPERIMENT(algs.ChangeGreedy, N, VN, 100000, PR3_exp_results_file)

# Algorithm 3: Change DP
with open(PR3_exp_results_file, 'a') as fw:
    fw.write("\nAlgorithm 3: Change Dynamic Programming\n")
print("\nAlgorithm 2: Change Dynamic Programming")

RUNEXPERIMENT(algs.ChangeDP, N, VN, 1000, PR3_exp_results_file)

# Question 4 - VM1

# # Algorithm 1: Change Slow
# with open(exp_results_file, 'a') as fw:
#    fw.write("\nAlgorithm 1: Change Slow\n")
# print("\nAlgorithm 1: Change Slow")

# RUNEXPERIMENT(algs.ChangeSlow, M, VM1, 1, exp_results_file)

# # Algorithm 2: Change Greedy
# with open(exp_results_file, 'a') as fw:
#    fw.write("\nAlgorithm 2: Change Greedy\n")
# print("\nAlgorithm 2: Change Greedy")

# RUNEXPERIMENT(algs.ChangeGreedy, M, VM1, 1, exp_results_file)

# # Algorithm 3: Change DP
# # with open(exp_results_file, 'a') as fw:
# #     fw.write("\nAlgorithm 3: Change DP\n")
# # print("\nAlgorithm 3: Change DP")
# # Using ML Targets
# # RUNEXPERIMENT(algs.ChangeDP, ML, VM1, 1, exp_results_file)

# # Question 4 - VM2

# # Algorithm 1: Change Slow
# with open(exp_results_file, 'a') as fw:
#    fw.write("\nAlgorithm 1: Change Slow\n")
# print("\nAlgorithm 1: Change Slow")

# RUNEXPERIMENT(algs.ChangeSlow, M, VM2, 1, exp_results_file)

# # Algorithm 2: Change Greedy
# with open(exp_results_file, 'a') as fw:
#    fw.write("\nAlgorithm 2: Change Greedy\n")
# print("\nAlgorithm 2: Change Greedy")

# RUNEXPERIMENT(algs.ChangeGreedy, M, VM2, 1, exp_results_file)

# # Algorithm 3: Change DP
# # with open(exp_results_file, 'a') as fw:
#       fw.write("\nAlgorithm 3: Change DP\n")
# # print("\nAlgorithm 3: Change DP")

# # RUNEXPERIMENT(algs.ChangeDP, ML, VM2, 1, exp_results_file)

