# Algorithm 1: Enumeration
def ChangeSlow(array, target):
    target = int(target)
    c = [0] * len(array)
    m = 0
    return c, m


# Algorithm 2: Change Greedy
def ChangeGreedy(array, target):
    #target = int(target)
    c = [0] * len(array)
    m = 0
    i = len(array) - 1
    for ea in reversed(array):
        while target - ea >= 0:
            target -= ea
            m += 1
            c[i]+= 1
        i -= 1
    return c, m


# Algorithm 3: Change Dynamic Programming
def ChangeDP(array, target):
    target = int(target)
    c = [0] * len(array)
    m = 0
    return c, m