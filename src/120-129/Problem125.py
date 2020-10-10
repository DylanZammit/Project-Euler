from math import sqrt
from math import log10

def first_dig(n): return n//10**int(log10(n)) if n !=0 else 0

def is_palindrome(n):
    n = str(n)
    L= len(n)
    for i in range(L//2):
        if n[i]!=n[L-i-1]:
            return False
    return True

B = 10**8

M = int(sqrt(B))+1

out = 0

checked = []

for i in range(1, M+1):
    for j in range(i+1, M+1):
        s = sum(x**2 for x in range(i, j+1))
        if s > B: break
        if is_palindrome(s) and s<B and s not in checked:
            checked.append(s)
            out+=s
print(out)