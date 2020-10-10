import numpy as np
import math

d=1000000

largest = 0
out = 0

for i in range(d, 0, -1):
    n = int(3/7*i)

    if n/i == 3/7:
        n-=1

    if largest < n/i:
        largest = n/i
        out = n//math.gcd(i, n)

print(out)
