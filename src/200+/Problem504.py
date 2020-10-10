from math import sqrt
import numpy as np
import time
start_time = time.time()

m=100
m=4

arr = np.zeros((m, m))

for i in range(m):
    for j in range(m):
        arr[i, j] = np.gcd(i+1, j+1)

out = m

temp = 0
for a in range(m):
    for b in range(a+1, m):
        for c in range(b+1, m):
            for d in range(c+1, m):
                z = arr[a, b]+arr[b, c]+arr[c, d]+arr[a, d]
                S = sqrt(z)
                if S == int(S):
                    temp+=1
out+=temp*4

temp = 0 
for a in range(m):
    for b in range(m):
        if a!=b:
            z = 2*arr[a, b]+2*b
            S = sqrt(z)
            if S == int(S):
                temp+=1
out+=temp*4

temp = 0
for a in range(m):
    for c in range(m):
        if a!=c:
            z = 2*arr[a, c]
            S = sqrt(z)
            if S == int(S):
                temp+=1
out+=temp*2

for a in range(m):
    for b in range(m):
        if a!=b:
            z = a+b+2*arr[a, b]
            S = sqrt(z)
            if S == int(S):
                temp+=1

out+=temp*4

for a in range(m):
    for c in range(m):
        for d in range(m):
            if c!=d and a!=c and d!=a:
                z = a+arr[a, c]+arr[c, d]+arr[a, d]
                S = sqrt(z)
                if S == int(S):
                    temp+=1

out+=temp*4

print(out, ': ', time.time()-start_time, 'secs')