from math import log
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

def M(p, q, N):

    g = p*q
    z = N/g
    x = int(log(z, p))
    y = int(log(z, q))
    
    maxi = g

    for i in range(x+1):
        for j in range(y+1):

            h = g*p**i*q**j

            if h > N: break

            if h > maxi:
                maxi = h
    return maxi

def S(N):
    out = 0
    n_p = len(primes)
    for i in range(n_p):
        for j in range(i+1, n_p):
            p = int(primes[i])
            q = int(primes[j])

            if p*q > N: break
            out+=M(p, q, N)
    return out

N = 10**7

primes = get_primes_less_than(N//2)

print(S(N), ': ', time.time()-start_time, 'secs')