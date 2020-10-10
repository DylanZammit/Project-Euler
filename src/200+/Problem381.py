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

def S(p):
    p=int(p)
    # https://math.stackexchange.com/questions/586595/finding-modular-of-a-fraction#:~:text=To%20find%20what%20number%20modulo,will%20give%20you%20b%E2%88%921.&text=After%20you%20know%20what%20b,%E2%88%921(modn).
    #(p-1)! = -1 = p-1 mod p
    #(p-2)! = (p-1)!/(p-1) = 1 mod 
    #(p-3)! = 1/(p-2) = (p-2)^(p-2)

    a = pow(p-2, p-2, p)
    b = pow(p-3, p-2, p)
    c = pow(p-4, p-2, p)

    out = p

    x = (a*b)%p
    y = (x*c)%p

    out+=a%p
    out+=x
    out+=y

    return out%p

M = 10**8

primes = get_primes_less_than(M)



print(sum(S(p) for p in primes[2:]), ': ', time.time()-start_time, 'secs')