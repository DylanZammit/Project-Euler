#Let p be a prime number. The number of binomial coeffucients nC0, nC1...nCn that are multiples of p is
# n + 1 - (n0 + 1)(n1 + 1)...(nr + 1);
# where n0 ... nr denote the digits in the expansion of n in base p.
import numpy as np
import time
from math import log

start_time = time.time()

def numberToBase(n, b=7):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

out=0
R = 10**9
# R=100
#https://math.mit.edu/research/highschool/rsi/documents/2017Puig.pdf

for n in range(R):
    if n%10**5==0: print(n)
    a = numberToBase(n)
    out += int(np.prod([x+1 for x in a]))

print(out, time.time()-start_time, 'secs')