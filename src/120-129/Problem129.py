import numpy as np

def A(n):
    k=1
    res = 1
    while True:
        res = (pow(10, k, n)+res)%n
        k+=1
        if res==0: return k

n=1000000
B=1000000
# B=10
a=0
while a<B:

    if(np.gcd(n, 10)==1):
        a=A(n)
        print(n, a)
    n+=1
print(n-1)