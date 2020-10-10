from math import log
import numpy as np
import time
start_time=time.time()

def get_primes_less_than(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

primes = get_primes_less_than(100)

out = 1

def rec(M, ind = 0):
    global out
    
    for i in range(ind, len(primes)):
        p = primes[i]
        U = int(log(M, p))
        out+=U
        for j in range(1, U+1):
            rec(M/p**j, i+1)

rec(10**9)
print(out, time.time()-start_time, 'secs')

