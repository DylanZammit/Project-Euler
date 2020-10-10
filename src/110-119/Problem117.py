stored = {}

def rec(n, L):
    if n < L: return 0

    out=n-L+1
    for i in range(n-L+1):
        for L in range(2, 5):
            if str((i, L)) not in stored:
                stored[str((i, L))]=rec(i, L)
            out+=stored[str((i, L))]
    return out

n=50

print(sum(rec(n, L) for L in range(2, 5))+1)