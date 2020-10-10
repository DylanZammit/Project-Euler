# # Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. 
# # For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
from math import sqrt
import time
start_time = time.time()

M = 10**7

fact_ct = [0]*M

# for n in range(2, int(sqrt(M)+1)):
for n in range(2, M//2):
    for i in range(n*2, M, n):
        fact_ct[i]+=1
        
print(sum(fact_ct[i]==fact_ct[i+1] for i in range(len(fact_ct)-1))-2)
print(float(time.time()-start_time), "secs")