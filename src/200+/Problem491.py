import itertools
import time
from math import factorial
from collections import Counter

start_time = time.time()

digits = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
# digits = [1, 1, 2, 2, 3, 3]

out=0

L = len(digits)

f_10 = factorial(10)
f_9 = factorial(9)

A = f_10**2+(f_10/2-f_9)*f_10
B = 2*(f_10-f_9)*f_10

for comb in itertools.combinations(digits, L//2):
    
    x = Counter(list(comb))

    m1 = 2**sum(x[y]==2 for y in x)
    m2 = 2**sum(x[y]==0 for y in x)
    
    z = 0
    for digit in x:
        if x[digit]==0: z-=2*digit
        elif x[digit]==2: z+=2*digit
    if z%11==0: 
        print(comb)
        if x[0] == 0 or x[0] == 2:
            out += f_10**2/(m1*m2) + (f_10/m2-f_9/m2)*f_10/m1
        else:
            out += (f_10/m1-f_9/m1)*f_10/m2 + (f_10/m2-f_9/m2)*f_10/m1

print(out,time.time()-start_time, 'secs')

# print(out)