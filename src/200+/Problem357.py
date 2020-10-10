from math import sqrt
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

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1
def is_prime(n):
    if n==2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def are_divs_prime(n):
    if n%4==0: return False 
    S = sqrt(n)
    for i in range(2, int(S)+1):
        if n%i==0:
            if binary_search(all_primes, i+n//i)==-1:
                return False
    return True
    
M=10**8
# M=100
all_primes = get_primes_less_than(2*M)

ind = next(x[0] for x in enumerate(all_primes) if x[1] > (M+4)//2)

primes = all_primes[:ind]
# print(len(primes))

out=0
count = 0

for q in all_primes:
    p = 2*q-3
    if p-1 > M: break
    if (p-1)/2%2==1:
        if binary_search(all_primes, p)!=-1:
            if are_divs_prime(p-1): 
                # print(p-1)
                out+=int(p-1)
    if count%10**6==0: print(count)
    count+=1
       
print(out, time.time()-start_time, 'secs')