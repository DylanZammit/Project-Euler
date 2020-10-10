# https://www.ias.ac.in/article/fulltext/reso/015/12/1111-1121
# https://www.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html#:~:text=In%20general%2C%20if%20you%20have,%3A%20Determine%20S(1800).


from math import log
import numpy as np
import time
start_time  = time.time()

def get_primes_less_than(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

def does_divide_Bn(p):
    for m in range(1, p):
        z = log((n+1)/m, p)

        if z==int(z):
            return False
    return True


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def D(n):
    if n%1000==0: print(n)
    s_i = 1
    for p in primes:
        p=int(p)
        if p > n: break
        n_p = numberToBase(n, p)

        k = n+1-int(np.prod([n_i+1 for n_i in n_p]))
        
        s_i *= ((p**(k+1)-1)//(p-1))%M
    return s_i%M

def S(n):
    return sum(D(k) for k in range(1, n+1))

M = 1000000007
n = 20000
n=5

primes = get_primes_less_than(2*n+1)
out = 0

print(S(n), ': ', time.time()-start_time, 'secs')
        
