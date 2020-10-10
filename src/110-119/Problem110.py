import numpy as np
from math import sqrt, log
from itertools import combinations
import itertools

def get_primes_less_than(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

primes = get_primes_less_than(10**7)


def num_sols(ps):
    ps = [int(2*v+1) for v in ps]
    out = 1
    for p in ps:
        out*=p
    return (out+1)//2

def to_num(ps):
    out=1
    for i in range(len(ps)):
        out*=int(int(primes[i])**ps[i])
    return out

mini=10**30
def temp(n, ind, U, a=[]):
    global mini
    rem = n-len(a)
    if rem==0:
        if num_sols(a) > M:
            T = to_num(a)
            if T < mini:
                mini = T
                print(mini)
    else:
        for i in range(min(ind+1, U[n-rem])):
            temp(n, i, U, a+[i])

def start_algo(n, M):
    U=[]
    for i in range(n):
        U.append(int(log(M, primes[i]))+1)
    temp(n, U[0], U)

n=20
M=4000000
# M=1000
start_algo(n, M)
print(mini)