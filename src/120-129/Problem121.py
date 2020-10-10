import itertools
import numpy as np
from math import factorial
from decimal import *
getcontext().prec = 50

num_rounds = 15
min_blue = num_rounds//2+1

num = 1

for C in range(1, num_rounds - min_blue+1):
    for comb in itertools.combinations(list(range(1, num_rounds+1)), C):
        # print(comb)
        num += int(np.prod(comb))
        
p_win = Decimal(int(num))/Decimal(int(factorial(num_rounds+1)))
print(p_win)
print(1/p_win)

