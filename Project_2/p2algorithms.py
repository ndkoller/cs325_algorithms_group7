# Algorithm 1: Enumeration
# Helper function
def change(target, coins, coins_list):
    if sum(coins_list) == target:
        yield coins_list
    elif sum(coins_list) > target:
        pass
    elif coins == []:
        pass
    else:
        for c in change(target, coins[:], coins_list + [coins[0]]):
            yield c
        for c in change(target, coins[1:], coins_list):
            yield c

def ChangeSlow(coins, target):
    # Call helper function and create list of all solutions
    solutions = [s for s in change(target, coins, [])]

    # optimal solution
    opt = min(solutions, key=len)
    m = len(opt)

    c = [0] * len(coins)
    i = 0
    for ea in coins:
        c[i] = opt.count(ea)
        i += 1

    return c, m


# Algorithm 2: Change Greedy
def ChangeGreedy(array, target):
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