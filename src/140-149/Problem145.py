from math import log10

def reverse(n):
	rev = 0
	while n!=0:
		r=int(n%10)
		rev = rev*10 + r
		n=int(n/10)
	return rev

def are_all_odd(n):
    L = int(log10(n))+1

    for i in range(L):
        if (n%10)%2==0:
            return False
        n//=10
    return True

def first_dig(n): return n//10**int(log10(n))
def sec_dig(n): return first_dig(n-first_dig(n)*10**int(log10(n)))
def third_dig(n): return first_dig(n-sec_dig(n)*10**int(log10(n)))
def last_dig(n): return n%10

M = 1000
M = 10**9
out = 0


for n in range(1, M+1):
    if n%10!=0:
        if first_dig(n)%2 != last_dig(n)%2:
            rev = reverse(n)
            if are_all_odd(n+rev):
                out+=1
                # print(n,'+',rev,'=',n+rev)
    if n%1000000==0: print(n)

print(out)