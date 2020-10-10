from math import log10

a, b, lim, out = 3, 2, 1000, 0

for i in range(lim):

    a, b = 2*b+a, b+a

    if int(log10(a)) > int(log10(b)): out+=1

print(out)
