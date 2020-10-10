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

M = 10**8
sqrt_M = int(np.sqrt(M))+1


primes = get_primes_less_than(M)
N = len(primes)

res = next(x for x, val in enumerate(primes) if val > sqrt_M) 

primes_sqrt = primes[:res]
N0 = len(primes_sqrt)

primes = primes[res:]

out=(N0**2+N0)//2

for p in primes:
    for p0 in primes_sqrt:
        if p*p0<=M:
            out+=1
        else: break
print(out, ': ', float(time.time()-start_time), 'secs')