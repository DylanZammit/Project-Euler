#1 = +
#2 = -
#3 = *
#4 = /

#brack: choose 0<=a<b<=3

import numpy as np   
from itertools import permutations        

def solve(oper, digits):
    if len(digits)==1: return digits[0]
    if len(oper)==1:
        if(oper[0] == 0): return digits[0]+digits[1]
        if(oper[0] == 1): return digits[0]-digits[1]
        if(oper[0] == 2): return digits[0]*digits[1]
        if(oper[0] == 3): return digits[0]/digits[1]
        
    if(oper[0]==2 and oper[1]==2):
        return digits[0]*digits[1]*digits[2]
    if(oper[0]==2 and oper[1]==3):
        return digits[0]*digits[1]/digits[2]
    if(oper[0]==3 and oper[1]==2):
        return digits[0]/digits[1]*digits[2]
    if(oper[0]==3 and oper[1]==3):
        return digits[0]/digits[1]/digits[2]
    if(oper[0]==0 and oper[1]==0):
        return digits[0]+digits[1]+digits[2]
    if(oper[0]==0 and oper[1]==1):
        return digits[0]+digits[1]-digits[2]
    if(oper[0]==1 and oper[1]==0):
        return digits[0]-digits[1]+digits[2]
    if(oper[0]==1 and oper[1]==1):
        return digits[0]-digits[1]-digits[2]

    if(oper[0]==0):
        return digits[0]+solve([oper[1]], [digits[1], digits[2]])
    if(oper[0]==1):
        return digits[0]-solve([oper[1]], [digits[1], digits[2]])
    if(oper[1]==0):
        return solve([oper[0]], [digits[0], digits[1]])+digits[2]
    if(oper[1]==1):
        return solve([oper[0]], [digits[0], digits[1]])-digits[2]
    
                
def get_max(arr):
    arr = np.sort(arr)

    for i in range(len(arr)):
        if(i+1 not in arr): return i

max_val = 0
max_arg = []

for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                
                distinct_out = []

                digits = [a, b, c, d]

                permutations_object = permutations(digits)
                permutations_list = list(permutations_object)

                for perm in permutations_list:
                    perm=list(perm)

                    #oper
                    for x in range(4):
                        for y in range(4):
                            for z in range(4):
                                
                                oper = [x, y, z]

                                #bracket
                                for b1 in range(3):
                                    for b2 in range(b1+1, 4):
                                        brack = solve(oper[b1:b2-1], perm[b1:b2])
                                        
                                        new_oper = oper[:b1]+oper[b2-1:]
                                        new_digits = perm[:b1]+[brack]+perm[b2:]

                                        ans = solve(new_oper, new_digits)

                                        if(ans not in distinct_out and ans==int(ans) and ans > 0): distinct_out.append(ans)

                n = get_max(distinct_out)
                if n > max_val:
                    max_val = n
                    max_arg = [a, b, c, d]
print(max_arg)


                     