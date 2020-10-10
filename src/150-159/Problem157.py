# Consider the diophantine equation 1/a+1/b= p/10n with a, b, p, n positive integers and a ≤ b.
# How many solutions has this equation for 1 ≤ n ≤ 9?
from math import sqrt
import time
start_time = time.time()

M = 10**9
M=10

fact_ct = [0]*M

# for n in range(2, int(sqrt(M)+1)):
for n in range(2, M//2):
    for i in range(n*2, M, n):
        fact_ct[i]+=1
        
print(fact_ct, float(time.time()-start_time), "secs")