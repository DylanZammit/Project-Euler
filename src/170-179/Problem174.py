from math import sqrt

def main(M):
    a_max = int(M/4+1)+1
    
    out = {}
    
    for a in range(3, a_max):
        b_min = int(sqrt(a**2-M)) if a**2 >= M else 1 + 1*(a%2==0)
    
        for b in range(a-2, max(1, b_min)-1, -2):
            t = a**2 - b**2
            out[t] = out.get(t, 0) + 1
    
    out = dict(sorted(out.items()))
    return out


def N(n, out):
    return len({k: v for k, v in out.items() if v == n and k <= M})

if __name__ == '__main__':
    M = 1_000_000
    
    out = main(M)
    for n in range(1, 16):
        print(f'N({n}) = {N(n, out)}')
    
    print(N(15, out)) # 832
    
    print(sum([N(n, out) for n in range(1, 11)]))


