import numpy as np
from math import log2

def num_of_factors(n):
    out = [0]
    count = 0
    while n>1:
        p=primes[count]
        if n%p==0: 
            # out.append(p)
            out[-1]+=1
            n//=p
        else:
            out.append(0)
            count+=1
    return int(np.prod([x+1 for x in out]))

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

def get_primes_less_than(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

primes = get_primes_less_than(100000)

found = set()

for n in range(1, 100000):
    z = num_of_factors(n)
    if z not in found and log2(z)==int(log2(z)):
        print(n, z, get_prime_factors(n))
        found.add(z)

pows = [1]

M=500500
M=16

for i in range(M+1):
    pow_sets = set(pows)

    compare_pows = []

    for pow_ in pow_sets:

        # p = primes[first of pow_]

        b=log2(pow_+1)+1
        next_pow = 2**b-1
        a=p**(next_pow-b)
        compare_pows.append(a)
    x = 
# out = 8
# n=500500
# n=7
# for i in range(3, 2*n-1, 2):
#     out=(out*i)%500500507
# print(out)