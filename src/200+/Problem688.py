M = 1000000007

def s(n):
    return n*(n+1)//2

def f(n, k):
    z = n//k
    while z>0:
        if s(z+k-1)-s(z-1) <= n:
            return z%M
        z-=1
    return z

def F(n):
    return sum(f(n, k) for k in range(1, n+1))

def S(N):
    return sum(F(n) for n in range(1, N+1))

N = 10**16

print(S(N))