from math import sqrt, log10
import time

start_time = time.time()

def is_prime(n):
    if n==2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True

def sum_dig(n):
    sum_dig=0
    for i in range(int(log10(n)+1)):
        sum_dig+=n%10
        n//=10
    return sum_dig

out = 0

B = 14
found = set([0])

def find_rthp(n):
    global out
    if int(log10(n))+1==B: return

    should_check = is_prime(n//sum_dig(n))

    for i in range(10):
        z=n*10+i
        if should_check:
            if is_prime(z):
                found.add(z)
        sd = sum_dig(z)
        if z%sd==0:
            find_rthp(z)

for n in range(1, 10):
    find_rthp(n)

print(sum(found), time.time()-start_time, 'secs')