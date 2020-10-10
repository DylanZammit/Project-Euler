# from math import sqrt
# import numpy as np

# def partition(collection):
#     if len(collection) == 1:
#         yield [ collection ]
#         return

#     first = collection[0]
#     for smaller in partition(collection[1:]):
#         for n, subset in enumerate(smaller):
#             yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
#         yield [ [ first ] ] + smaller

# def is_prime(n):
#     if n==2: return True
#     if n%2==0: return False

#     for i in range(3, int(sqrt(n))+1, 2):
#         if n%i==0: return False
#     return True

# def gen_primes(M):
#     out = []
#     for i in range(2, M):
#         if is_prime(i): out.append(i)
#     return out

# def get_prime_factors(n):
#     out = []
#     count = 0
#     while n>1:
#         p=primes[count]
#         if n%p==0: 
#             out.append(p)
#             n//=p
#         else:
#             count+=1
#     return out

# def gen_prime_factors(M):
#     out = []
#     for i in range(2, M):
#         out.append(get_prime_factors(i))
#     return out

# M=12000
# primes = gen_primes(14000)
# prime_factors = gen_prime_factors(14000)

# jumbles = {}

# def part(pfs):

#     mix=[]
#     N = len(pfs)

#     arr = list(range(N))
#     if str(N) not in jumbles:
#         for n, p in enumerate(partition(arr), 1):
#             mix.append(sorted(p))
#     else:
#         mix = jumbles[str(N)]

#     out=[]
#     for mm in mix:
#         temp2 = []
#         for m in mm:
#             temp = []
#             for t in m:
#                 temp.append(pfs[t])
#             temp2.append(temp)
#         out.append(temp2)
    
#     return out
# # part([2, 3, 3, 5])

# def run_here(k):
#     z=k
#     while True:
#         prime_facts = prime_factors[z-2]
#         pf_parts = part(prime_facts)
#         for pf in pf_parts:
            
#             Q = [np.prod(p) for p in pf]
#             L = len(Q)
#             if z - sum(Q) == k-L:
#                 print(k, z, Q)
#                 return z
#         z+=1

# ans = 0
# m=12000
# # m=12
# vals=[]
# for k in range(2, m+1):
#     vals.append(run_here(k))
#     if k%100==0: print(k)
# vals = list(set(vals))
# print('=========')
# print(sum(vals))

#####################################################

# from math import sqrt
# from numpy import prod
# import time
# start_time = time.time()

# def get_factor_pairs(n):
#     factors = []
#     S = sqrt(n)

#     for i in range(2, int(S)+1):
#         if n%i==0:
#             factors.append([i,n//i])
#     return factors

# def is_prime(n):
#     if n==2: return True
#     if n%2==0 or n==1: return False

#     for i in range(3, int(sqrt(n))+1, 2):
#         if n%i==0: return False
#     return True

# fact_pairs_dict={}

# are_prime = {}

# def exist_part(k, z, a, s, n):
#     if z==s+k-n:
#         return True
#     elif z<s+k-n:
#         for ai in a:
#             ss = str(ai)
#             if ss not in are_prime:
#                 are_prime[ss]=is_prime(ai)

#             # if not is_prime(ai):
#             if not are_prime[ss]:

#                 if ss not in fact_pairs_dict:
#                     fact_pairs_dict[ss] = get_factor_pairs(ai)
#                 fact_pairs = fact_pairs_dict[ss]

#                 for fp in fact_pairs:
#                     ind = a.index(ai)
#                     if exist_part(k, z, a[:ind]+[fp[0], fp[1]]+ a[ind+1:], s-ai+sum(fp), n+1):
#                         return True
#     return False

# M=12000
# # M=12
# out = []
# k=2

# while k<M+1:
#     z=k+1
#     while not exist_part(k, z, [z], z, 1):
#         z+=1
#     # print(k, z)
#     out.append(z)
#     if k%100==0:
#         # print(k)
#         t = time.time() - start_time
#         print(k, "%s seconds" % t)
#     k+=1
# print(sum(set(out)))

#####################################################
from math import sqrt
import numpy as np

def get_primes_less_than(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    pp = 2*np.nonzero(sieve)[0][1::]+1
    pp = np.insert(pp, 0, 2)
    return pp



def get_prime_factors(n):
    out = []
    count = 0
    while n>1:
        p=primes[count]
        if n%p==0: 
            out.append(p)
            n//=p
        else:
            count+=1
    return out

def gen_prime_factors(M):
    out = []
    for i in range(2, M):
        out.append(get_prime_factors(i))
    return out

M=24000
primes = get_primes_less_than(M)
prime_factors = gen_prime_factors(M)

for prime_factor in prime_factors:
    for i in range(len(prime_factor)):
