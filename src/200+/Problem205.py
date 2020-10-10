import numpy as np

P = list(range(1, 5))
C = list(range(1, 7))

Pp = [1/4]*4
Cp = [1/6]*6

X1p = Pp.copy()
X2p = Cp.copy()

P_final = P.copy()
C_final = C.copy()

Np = 9
Nc = 6

P_final = list(range(Np,Np*4+1))
C_final = list(range(Nc,Nc*6+1))

for _ in range(Np-1):
    X1p = np.convolve(X1p, Pp)
for _ in range(Nc-1):
    X2p = np.convolve(X2p, Cp)

out = 0
for i in range(len(X1p)):
    temp = 0
    for j in range(len(X2p)):
        if C_final[j]<P_final[i]:
            temp+=X2p[j]
    out+=temp*X1p[i]

print(len(X1p), len(P_final))
print(len(X2p), len(C_final))
print(out)
