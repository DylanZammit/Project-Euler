from math import *
import time
start_time = time.time()

def is_prime(n):
    if n == 2: return True
    if n%2==0 or n==1: return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0: return False
    return True


def are_concats_prime(a, b):
    La=int(log10(a))+1
    Lb=int(log10(b))+1

    x=a*10**Lb+b
    y=b*10**La+a

    return is_prime(x) and is_prime(y)

pair_primes = []
pair_not_primes = []

def are_pairs_prime(arr):
    L=len(arr)
    
    temp = []
    for i in range(L):
        for j in range(i+1, L):
            if (arr[i], arr[j]) in pair_not_primes:
                return False
            
            if (arr[i], arr[j]) not in pair_primes:
                if not are_concats_prime(arr[i], arr[j]): 
                    pair_not_primes.append((arr[i], arr[j]))
                    return False
                pair_primes.append((arr[i], arr[j]))
                
    return True


def temp_check(temp):
    for i in range(len(temp)-1):
        if not are_concats_prime(temp[i], temp[-1]): return False
    return True

def gen_primes(m):
    primes=[]
    for i in range(1, m):
        if is_prime(i): primes.append(i)
    return primes

primes = gen_primes(20000)

L = len(primes)

prr = False
for a in range(L-1):
    prr = True
    for b in range(a+1, L-1):
        temp = [primes[a]]
        if temp_check(temp+[primes[b]]):
            for c in range(b+1, L-1):
                temp = [primes[a], primes[b]]
                if temp_check(temp+[primes[c]]):
                    for d in range(c+1, L-1):
                        temp = [primes[a], primes[b], primes[c]]
                        if temp_check(temp+[primes[d]]):
                            for e in range(d+1, L-1):
                                temp = [primes[a], primes[b], primes[c], primes[d]]
                                if prr:
                                    prr=False
                                    print(temp)
                                if temp_check(temp+[primes[e]]):
                                    temp+=[primes[e]]
                                    print(temp)
                                    print(sum(temp))
                                    print("--- %s seconds ---" % (time.time() - start_time))  
