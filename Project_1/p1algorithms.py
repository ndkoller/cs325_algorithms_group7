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


# Algorithm 3: Divide and Conquer
def MAXSUBARRAY_DnC(array):
    max_sum = 0
    # Code
    return array[:], max_sum


# Algorithm 4: Linear Time
def MAXSUBARRAY_Linear(array):
    max_sum = 0
    # Code
    return array[:], max_sum