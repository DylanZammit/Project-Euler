import numpy as np
import math

lengths = {}

cap = 1500000

for n in range(1, int(np.ceil(np.sqrt(cap)))):

    for m in range(n, int(np.ceil(np.sqrt(cap)))):

        if math.gcd(m, n) == 1 and (m%2==0 or n%2==0):

            a0, b0, c0 = m**2-n**2, 2*m*n, m**2+n**2
            
            L = a0+b0+c0

            a, b, c, = a0, b0, c0

            d = 2
            while L <= cap:

                lengths[str(L)] = lengths[str(L)]+1 if str(L) in lengths else 1
                
                a, b, c = d*a0, d*b0, d*c0

                L = a+b+c

                d+=1
            

print(sum([lengths[x]==1 for x in lengths]))