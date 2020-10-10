import numpy as np
from math import log10
from math import sqrt
from itertools import *

def is_prime(n):
    
    if n==2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def get_primes_less_than(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

def num_to_arr(n):
    out = []
    L = int(log10(n))+1
    for _ in range(L):
        out.append(n%10)
        n//=10
    out.reverse()
    return out

def is_valid(p, rem):
    if len(p)!=len(set(p)): return False
    for i in p:
        if i not in rem: return False
    return True

# primes = get_primes_less_than(10**9)

# t = []

# def check_rep(s):
#     for c in s:
#         if s.count(c)>1: return True
#     return False

# for p in primes:
#     if not check_rep(str(p)):
#         t.append(p)


def get_n_dig_pal_primes(n):
    out = []
    digits = list(range(1,10))
    for comb in list(combinations(digits, n)):
        for num in list(permutations(comb)):
            strings = [str(integer) for integer in num]
            a_string = "".join(strings)
            p = int(a_string)
            if is_prime(p): out.append(p)
    
    return np.sort(out)

primes=[]
for n in range(1, 10):
    primes+=list(get_n_dig_pal_primes(n))

primes.reverse()
N=len(primes)
print(N)
count=0
def f(rem=list(range(1, 10)), pos=0):#, arr=[]):
    global count
    if len(rem)==0:
        count+=1
        if(count%100==0): print(count)
        # print(arr)
    else:
        for i in range(pos, N):
            p=num_to_arr(primes[i])
            if is_valid(p, rem):
                # temp=arr.copy()
                # temp.append(primes[i])
                f(set(rem).difference(set(p)), i+1)#, temp)

# f()


# digits = list(range(1, 10))
# for num in list(permutations(digits)):
#     strings = [str(integer) for integer in num]
#     a_string = "".join(strings)
#     p = int(a_string)
    
#     for i in range(1, 8):
#         split(num, i)

print(count)