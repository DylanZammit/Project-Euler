from numpy import linalg as LA
import numpy as np
from math import sqrt

M=50

T = (M+1)**2

def is_right(a, b):

    #if colinear
    if(a[1]*(b[1]-b[0])==b[1]*(a[1]-a[0])): return False

    d1 = (a[0]-b[0])**2+(a[1]-b[1])**2
    d2 = a[0]**2+a[1]**2
    d3 = b[0]**2+b[1]**2

    d=max(d1, d2, d3)

    return d==d1+d2+d3-d

ans=0

for i in range(1, T):
    for j in range(i+1, T):
        x1=i//(M+1)
        y1=i%(M+1)

        x2=j//(M+1)
        y2=j%(M+1)

        p1 = np.array([x1, y1])
        p2 = np.array([x2, y2])

        if(is_right(p1, p2)):
            ans+=1
print(ans)

