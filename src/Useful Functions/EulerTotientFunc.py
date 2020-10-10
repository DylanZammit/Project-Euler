import numpy as np

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if np.gcd(x, y)==1]
        return len(n)