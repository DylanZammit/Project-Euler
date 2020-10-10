out = 0

B=10000

for a in range(3, 1001):
    r=[]

    for n in range(1, B):
        r.append(2*a*n%a**2)

    out+=max(r)
print(out)
