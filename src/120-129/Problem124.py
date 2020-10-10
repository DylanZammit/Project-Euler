# from PrimeFunctions import *
import numpy as np
from math import sqrt

def is_prime(n):
    if n==2: return True
    if n%2==0: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

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

def gen_prime_factors(M):
    out = []
    for i in range(2, M):
        out.append(get_prime_factors(i))
        if i%10000==0: print(i)
    return out

M=100000

primes = gen_primes(M+1)

prime_factors = gen_prime_factors(M+1)

prime_factors = [np.prod(list(set(p))) for p in prime_factors]
indices = np.array([i for i in range(2, len(prime_factors)+2)])

mat = np.insert(np.transpose([indices, prime_factors]), 0, np.array((1, 1)), 0) 
mat = [tuple(mat[v,:]) for v in range(len(mat))]
dtype=[('n', int), ('p', int)]
mat=np.array(mat, dtype=dtype)
mat=np.sort(mat, order = ['p', 'n'])

ans_ind=10000

print(mat[ans_ind-1])