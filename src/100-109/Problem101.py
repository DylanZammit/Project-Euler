import numpy as np

def u(n): return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

out = 0

for i in range(2, 10+2):
    x=list(range(1, i))
    y=[u(z) for z in x]
    z = np.polyfit(x, y, len(y)-1)
    p = np.poly1d(z)
    out+=round(p(i))
print(int(out))