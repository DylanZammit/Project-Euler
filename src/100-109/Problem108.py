from math import sqrt
import numpy as np
from itertools import zip_longest

def is_prime(n):
    if n==2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def get_prime_factors(n):
    m=n
    out = [0]
    count = 0
    while n>1:
        p=primes[count]
        if n%p==0:
            out[-1]+=1
            n//=p
        else:
            out.append(0)
            count+=1
        if str(n) in powers:
            out = [x + y for x, y in zip_longest(out, powers[str(n)], fillvalue=0)]
            n=1

    powers[str(m)] = out
    return out


def num_factors(n):
    out = 1
    power = 1
    count = 0
    while n>1:
        p=primes[count]
        if n%p==0:
            power+=1
            n//=p
            if n==1:
                out*=power
        else:
            out*=power
            power=1
            count+=1
    return (out+1)//2

def get_primes_less_than(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

powers = {}

def test2(n):
    powers = get_prime_factors(n**2)
    B = np.prod([x+1 for x in powers])
    return (B+1)//2

primes = get_primes_less_than(10**7)

n=2
M=4*10**6
M=1000
while test2(n) < M:
# while num_factors(n**2) < M:
    if(n%10==0): print(n, test2(n))
    n+=1
print(n)