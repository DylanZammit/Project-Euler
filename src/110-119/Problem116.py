stored = {}
n=50

def rec(n, L):
    out=n-L+1
    for i in range(L, n-L+1):
        if str(i) not in stored:
            stored[str(i)]=rec(i, L)
        out+=stored[str(i)]
    return out

ans = 0
M=4
for L in range(2, M+1): 
    stored = {}
    ans+=rec(n, L)
print(ans)