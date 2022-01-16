from math import factorial
from numpy import isnan

def progress(i, N, extra=''):
    pct = int(i/N*100)
    if pct!=int((i-1)/N*100):
        print(f'{pct}%', extra, end='\r')

p = 1_000_000_007
def A(k, n):
    M = int(k/2)+1

    out = 0
    f0 = 1
    for i in range(M):
        progress(i, M, out)
        out += pow(2, (k-2*i)*n//k, p)*f0
        out %= p
        n0 = (f0*((k-2*i-1)*(k-2*i))%p)%p
        d0 = pow(i+1, 2*(p-2), p)
        f0 = (n0*d0)%p

    print()
    return int(out%p)

k, n = 10**8, 10**16

print(A(3,9))
print(A(4,20))
print(A(k, n))


