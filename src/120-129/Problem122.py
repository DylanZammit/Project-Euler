found = False
best = 0
a=[1]
n=0

def backtrack(step):
    global found, a, n, best
    if not found:
        if a[step]==n:
            if step < best:
                best = step
                # chain = a
                found = True
                return
        else:
            if step < d:
                for i in range(step, -1, -1):
                    if 2*a[i]>a[step]:
                        for j in range(i, -1, -1):
                            k=a[i]+a[j]
                            a[step+1]=k
                            if a[step] < k <= n:
                                backtrack(step+1)

out=0
for n in range(1, 201):
    if n%20==0: print(n)
    best = n+1
    found = False
    d=1
    while not found:
        a=[1]*200
        backtrack(0)
        d+=1
    out+=(best)
print(out)