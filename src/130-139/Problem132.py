#If n is divisible by a, then Rn is divisible by Ra

from math import sqrt
import numpy as np

def is_prime(n):
    if n==2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def get_factors(n):
    factors = [1, n]
    S = sqrt(n)
    if int(S)==S:
        factors.append(S)
    for i in range(2, int(S)):
        if n%i==0:
            factors.append(i)
            factors.append(n//i)
    return factors

def gen_primes(M):
    out = []
    for i in range(2, M):
        if is_prime(i): out.append(i)
    return out

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

def R(n): return (10**n-1)//9

B = 10**9

primes = get_primes_less_than(10**9)

n_facts = get_factors(B)

n_facts = sorted(n_facts)

pf_ans = []

for n_fact in n_facts:
    r = R(n_fact)
    print(n_fact, r)
    pf = get_prime_factors(r)
    for p in pf:
        if p not in pf_ans or len(pf_ans)==40:
            pf_ans.append(p)
            print(pf_ans)
        if len(pf_ans)==40:
            print(sum(pf_ans))
            break

print(sum(pf_ans))
