import math
import numpy as np

a_s=[2, 1]

k=1
for i in range(100):
    if(i%3==0):
        a_s.append(2*k)
        k+=1
    else:
        a_s.append(1)
print(a_s)

pos=100

h0 = 0
h1 = 1

for x in range(pos):
    h2=a_s[x]*h1+h0

    h0=h1
    h1=h2

print(sum(int(dig) for dig in str(h1)))
    
