from math import log, sqrt
import time
start_time = time.time()

strong_repunits = set([1])

M = 10**12

for b in range(2, M):
    K = log(M*(b-1)+1, b)-1
    R = int(K)
    if R < 2: break

    for r in range(2, R+1):
        z = (b**(r+1)-1)//(b-1)
        if z not in strong_repunits and z!=b+1:
            strong_repunits.add(z)

print(sum(strong_repunits),': ', time.time()- start_time, 'secs')