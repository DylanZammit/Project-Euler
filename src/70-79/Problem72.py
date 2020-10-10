from math import sqrt

phi={
    '1': 1,
    '2': 2
}

def find_smallest_fact(n):
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0): return i
    return n

def gcd(p,q):
    
    while q != 0:
        p, q = q, p%q
    return p

def phi_func(n):
    a=find_smallest_fact(n)

    if(a!=n):
        b=int(n/a)

        d=gcd(a, b)
        out = phi[str(a)]*phi[str(b)]*d/phi[str(d)]
    else:
        out=n*(1-1/n)

    phi[str(n)]=out
    return out

d=1000000

out=0
for i in range(2, d+1):
    out+=phi_func(i)

print(out)