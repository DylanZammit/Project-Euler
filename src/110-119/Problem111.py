from math import sqrt, log10
from itertools import combinations, permutations, product
  
def findsubsets_comb(s, n): return list(combinations(s, n)) 
def findsubsets_perm(s, n): return list(product(s, repeat=n)) 

def is_prime(n):
    if n==2: return True
    if n%2==0 or n==1: return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def arr_to_num(arr):
    out=0
    for i in range(len(arr)):
        out*=10
        out+=arr[i]
    return out

n = 10
#5: 6045857
# n = 5
out = 0
print('d', 'M', 'N', '     S')
print('----------------')
for d in range(10):
    M=n+1
    S=0
    N=0
    while S==0:
        M-=1
        for ph_indices in findsubsets_comb(range(n), n-M):
            a = set(range(10))
            b = set([d])
            for ph_digits in findsubsets_perm(a.difference(b), n-M):
                num = [d]*n
                for j in range(n-M):
                    num[ph_indices[j]]=ph_digits[j]
                
                if num[0]!=0:
                    num = arr_to_num(num)
                    if is_prime(num):
                        S+=num
                        N+=1
    
    print(d, M+1, N, S)
    out+=S

print(out)