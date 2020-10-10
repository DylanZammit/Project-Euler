from math import factorial

def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

M=4

out = -1

def noa(n, ind=0):
    global out

    if n==0: return 

    out+=2**(ind+1)

    for length in range(3, n+1):
        for i in range(1, n-length+1):
            noa(n-length-i-1, i)

noa(4)
print(out)
n=4

out = out-(-2**n + 3**n - 2**(n-1)*n)#+(n-2)*nCr(n-3, 2)*3**(n-5)

out = 3**4-2*3-6*3**2

print(out)