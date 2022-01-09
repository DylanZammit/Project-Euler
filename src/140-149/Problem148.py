#Let p be a prime number. The number of binomial coeffucients nC0, nC1...nCn that are multiples of p is
# n + 1 - (n0 + 1)(n1 + 1)...(nr + 1);
# where n0 ... nr denote the digits in the expansion of n in base p.
import numpy as np
import time
from math import log

start_time = time.time()

def num2base(n, b=7):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def sup(n): return n*(n+1)/2

B = sup(7)
R = 10**9
A = num2base(R-1)
a = A[0]
z = len(A)

def f(x):
    z = len(x)
    out = B**(z-1)*(sup(x[0])-1)

    for i in range(z-1):
        T = np.prod([d+1 for d in x[:z-1-i]])*B**i
        T *= (sup(x[-1]+1) if i==0 else sup(x[z-1-i]))

        out += T
    return out

print('{}_10={}_7'.format(R, ''.join([str(x) for x in A])))
out = B**(z-1) + f(A)
print(int(out))
