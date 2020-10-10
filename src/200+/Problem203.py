from math import sqrt
import time

import operator as op
from functools import reduce

start_time=time.time()
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2
def get_factors(n):
    factors = [1, n]
    S = sqrt(n)
    
    for i in range(2, int(S)+1):
        if n%i==0:
            factors.append(i)
            if i!=n//i:
                factors.append(n//i)
    return factors

def is_prime(n):
    if n==2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def is_sq_free(n):
    factors = get_factors(n)
    for f in factors:
        S = sqrt(f)
        if S==int(S) and is_prime(S):
            return False
    return True
    
rows = 51

dist = [1]

for r in range(1, rows):
    for i in range(1, r//2+1):
        dist.append(ncr(r, i))
    
dist = list(set(dist))
out=0
L=len(dist)
for i in range(L):
    d=dist[i]
    print(i,'/', L)
    if is_sq_free(d):
        out+=d

print(out, time.time()-start_time, 'secs')
