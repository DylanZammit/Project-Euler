import numpy as np

factor_nums = {}

def get_next(n):

    if n not in factor_nums:
        factor_nums[n]=sum(get_factors(n))
        
    return factor_nums[n]

def get_factors(n):
    factors = [1]

    if n%2==0:
        factors.append(2)
        factors.append(n//2)

    for i in range(3, int(np.sqrt(n))):
        if n%i==0:
            factors.append(i)
            factors.append(n//i)
    return factors

largest = []

for start in range(20, 1000000):

    if start % 100000 == 0: print(start)

    curr = get_next(start)

    correct = True
    
    chain = [start]

    while curr != start:
        
        curr = get_next(curr)

        if curr == 1 or curr >= 1000000 or curr in chain[1:]:
            correct = False
            break

        chain.append(curr)

    if correct and len(largest) < len(chain):
        largest = [x for x in chain]

print(min(largest))