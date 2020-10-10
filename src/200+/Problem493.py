from decimal import *
from random import randint
import numpy as np

def choose(n, k):
    return Decimal(fact(n)/(fact(k)*fact(n-k)))

def fact(n):
    out=1
    for i in range(1, n+1):
        out*=i
    return out

def choose_rest(num_cols, out):

    for _ in range(9):
        out*=choose_rest(num_cols-1, out)
    
    if num_cols==0: return out

# T = sum([choose(7, k)*choose(9*k, 20-k) for k in range(2, 8)])

# exp = sum([k*choose(7, k)*choose(9*k, 20-k) for k in range(2, 8)])/T

# print(exp)

T = sum([choose(7, k)*choose_rest(k, 1) for k in range(2, 8)])

exp = sum([k*choose(7, k)*choose_rest(k, 1) for k in range(2, 8)])/T

print(exp)

def simulate(num_sims=1000, num_cols=7, num_cat=10, num_choose=20):
    
    num_dist=[]
    for _ in range(num_sims):
        balls = [num_cat]*num_cols
        for _ in range(num_choose):
            
            while True:
                r = randint(0, num_cols-1)

                if balls[r] > 0:
                    balls[r]-=1
                    break
        num_dist.append(sum([1 if x < num_cat else 0 for x in balls]))
    print(np.mean(num_dist))

simulate(num_sims=100000)