import numpy as np
import time
from decimal import *
getcontext().prec = 20

start_time = time.time()

def get_primes_less_than(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if gcd(x, y) == 1]
        return len(n)

def get_num(d):
    out = 0
    for i in range(1, d):
        if gcd(i, d)==1:
            out+=1
    return out
# def R(d): return get_num(d)/(d-1)
def R(d): return phi_func(d)/(d-1)

def get_ans():
    b=15499/94744
    # b=4/10
    d=2
    while True:

        print('R('+str(d)+')='+str(phi_func(d))+'/'+str(d-1), R(d))
        if R(d)<b:
            return d
        d+=1

primes = get_primes_less_than(24)

b=15499/94744
z=1
f=1
for p in primes:
    # if(p!=2):
    z=int(z)*int(p)
    f=int(p-1)*int(f)#p**(n-1)*
    print(p, z,':', Decimal(int(f))/Decimal(int(z-1)),'<', b,'?',Decimal(int(f))/Decimal(int(z-1)) < b )
    print(p, 2*z,':', Decimal(int(2*f))/Decimal(int(2*z-1)),'<', b,'?',Decimal(int(2*f))/Decimal(int(2*z-1)) < b )
    print(p, 4*z,':', Decimal(int(2*f))/Decimal(int(4*z-1)),'<', b,'?',Decimal(int(2*f))/Decimal(int(4*z-1)) < b )



# print(get_ans())
print("--- %s seconds ---" % (time.time() - start_time))