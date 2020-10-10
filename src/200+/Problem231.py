#use legendre's thm and kummers thm

import numpy as np
import time
start_time = time.time()

def get_primes_less_than(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

def numberOfCarryOperations(a, b, base):
    
    out = 0

    Na=len(a)
    Nb=len(b)

    if Na<Nb:
        a=[0]*(Nb-Na)+a
    if Na>Nb:
        b=[0]*(Na-Nb)+b

    N_min = min(Na, Nb)
    N_max = max(Na, Nb)
    
    carry = 0

    for i in range(N_max-1, -1, -1):
        if a[i]+b[i]+carry >= base:
            out+=1
            carry = 1
        else:
            carry = 0
    return out

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


n=20000000
m=15000000

z=n-m

primes = get_primes_less_than(n)

out=0
for p in primes:
    p=int(p)
    a = numberToBase(m, p)
    b = numberToBase(z, p)
    out+=p*numberOfCarryOperations(a, b, p)

print(out, time.time()-start_time, 'secs')