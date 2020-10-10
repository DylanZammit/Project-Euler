import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

n=100

out=2*nCr(10+n-1, n)

for i in range(1, n):
    out+=nCr(10+i-1, i)
out-=10*n-1

#minus 2 from asnwwer
print(out)