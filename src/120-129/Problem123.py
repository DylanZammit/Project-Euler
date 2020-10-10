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

primes = gen_primes(1000000)


i=0
B = 10**10
rem = 0
while rem <= B:
    pn=primes[i]
    n=i+1
    rem = (2*pn*n)%(pn**2)
    i+=1
print(n+1, rem)
