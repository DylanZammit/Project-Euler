from math import sqrt
import numpy as np

def get_primes_less_than(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

def get_prime_factors(n):
    out = []
    count = 0
    while n>1:
        p=primes[count]
        if n%p==0: 
            out.append(p)
            n//=p
        else:
            count+=1
    return out

def gen_prime_factors(M):
    out = []
    for i in range(2, M):
        out.append(get_prime_factors(i))
    return out

M=24000
primes = get_primes_less_than(M)
for k in range(2, 12000):
    print(f'{k}={int(k/12000*100)}%', end='\r')
    gen_prime_factors(k)

