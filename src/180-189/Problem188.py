B=10**8
a=1777
k=1855

out = 0
z=a
for _ in range(k-1):
    z = pow(a, z, B)
print(z)