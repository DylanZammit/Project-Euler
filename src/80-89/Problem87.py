from math import sqrt

primes=[2]

out={}

def f(p1,p2, p3):
    return p1**2+p2**3+p3**4

def is_prime(x):
    if(x==2): return True
    if(x%2==0): return False

    z=int(sqrt(x))
    for i in range(3, z+1, 2):
        if(x%i==0):
            return False
    return True

M=50000000
i=3
while True:
    if(is_prime(i)):
        primes.append(i)
        if(f(i, 2, 2)>M): break
    i+=2

ind_1=len(primes)-1

for i in range(ind_1+1):
    if(f(2, primes[i], 2)>M): break
ind_2=i

for i in range(ind_2+1):
    if(f(2, 2, primes[i])>M): break
ind_3=i

ans=0
for a in range(ind_1+1):
    for b in range(ind_2+1):
        for c in range(ind_3+1):
            val = f(primes[a], primes[b], primes[c])
            if(val < M):
                out[str(val)]=val
                ans+=1

print(len(out))

