from math import sqrt

M=10**6
out = 0

for n in range(1, M):
    if n%10000==0: print(n)
    n_sols = 0
    for d in range(int(sqrt(n/3)), n):
        if 36*d**2-20*d**2-4*n>0:
            x1 = (6*d+sqrt(36*d**2-20*d**2-4*n))/2
            x2 = (6*d-sqrt(36*d**2-20*d**2-4*n))/2

            if x1==int(x1): 
                # print(n, x1)
                n_sols+=1
            if x2==int(x2): 
                # print(n, x2)
                n_sols+=1
    if n_sols==10: out+=1
print(out)