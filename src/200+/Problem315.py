import numpy as np
from math import sqrt
import time

start_time = time.time()

digit_vals={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:4,8:7,9:6}
digit_rep={0: int('1111110', 2), 1: int('0110000', 2), 2: int('1101101', 2), 3: int('1111001', 2), 4: int('0110011', 2), 5: int('1011011', 2), 6: int('1011111', 2), 7: int('1110010', 2), 8: int('1111111', 2), 9: int('1111011', 2)}

s = np.zeros((10,10))

for i in range(10):
    for j in range(10):
        s[i, j] = int(sum(int(x) for x in bin(digit_rep[i]&digit_rep[j])[2:]))

trans = np.zeros((10,10))

for i in range(10):
    for j in range(10):
        trans[i, j] = digit_vals[i]+digit_vals[j]-2*s[i, j]

#sieve
def get_primes_less_than(n):
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp

def num2arr(n): return [int(d) for d in str(n)]

def pad(a0, a1):
    l0 = len(a0)
    l1 = len(a1)

    z = [-1]*abs(l1-l0)

    if l0 < l1:
        a0 = z + a0
    else:
        a1 = z + a1

    return a0, a1

def start(x0):

    out = sum(digit_vals[x] for x in num2arr(x0))
    naive = out*2

    while x0 >= 10:
        a0 = num2arr(x0)
        x1 = sum(a0)
        a1 = num2arr(x1)
        naive += sum(digit_vals[x] for x in a1)*2

        a0, a1 = pad(a0, a1)

        for i in range(len(a1)):
            if a0[i] == -1:
                out+=digit_vals[a1[i]]
            elif a1[i] == -1:
                out+=digit_vals[a0[i]]
            else:
                out+=trans[a0[i],a1[i]]
        x0=x1

    out+=digit_vals[x0]
    
    return out, naive

primes = get_primes_less_than(2*10**7)
primes = primes[primes>10**7]


out=0
for prime in primes:
    a, b = start(prime)
    out+=(b-a)

print(int(out), time.time()-start_time, 'secs')