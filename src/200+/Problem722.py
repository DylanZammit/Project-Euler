from math import sqrt

def get_factors(n):
    if n==1: return [1]
    out=[1, n]
    
    sq = sqrt(n)

    for i in range(2, int(sqrt(n))+1):
        if n%i==0: 
            out.append(i)
            if n//i != i:
                out.append(n//i)
    return out

def E(k, q, m=100000):
    out = 0
    for n in range(1, m):
        out+=s(k, n)*q**n
    return out

def s(k, n):
    divs = get_factors(n)
    
    out = 0
    for d in divs:
        out+=d**k
    return out

print(E(3, 1-2**(-8)))