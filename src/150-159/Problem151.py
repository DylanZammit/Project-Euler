# from random import randint
# import time
# start_time = time.time()

# N_sim = 10**5

# out = []

# for i in range(N_sim):
#     B = [2, 3, 4, 5]
#     immed_count = 0
#     for _ in range(14):
#         x=0
#         while x != 5:
#             # print(len(B))
#             if len(B)==1: immed_count+=1
#             x = B[randint(0, len(B)-1)]
#             if x != 5:
#                 B.remove(x)
#                 B+=[x+1, x+1]
#         B.remove(5)
#     out.append(immed_count)

# print(sum(out)/len(out), ': ', time.time()-start_time, 'secs')
#-----------------------------------------------

#https://math.stackexchange.com/questions/1895688/how-did-i-mix-up-this-expected-value-problem-project-euler-151
# should be around ~0.266
import time
from math import factorial
start_time = time.time()

def crack(n): return list(range(n+1, 6))

Env = [2, 3, 4, 5]

denom = 0
avg = 0

def rec(Env, n=14, curr_ct=0, p=1):#, arr=[]):
    global avg, denom

    M = len(Env)

    # if Env == [5]:
    #     # avg = (avg*denom+curr_ct)/(denom+1)
    #     avg = avg + p*curr_ct
    #     # denom += 1
    if len(Env) == n:
        f = factorial(n-1)

        no_singles = f*(n**2+n-2)//2
        one_single = f

        z=n*f

        avg += (curr_ct+1)*one_single*(1/z)*p+curr_ct*no_singles*(n-1)/z*p

        # avg = (avg*denom+curr_ct*no_singles+(curr_ct+1)*one_single)/(denom+no_singles+one_single)
        # denom+=(no_singles+one_single)
    else:
        
        for e in Env:
            new_env = Env.copy()
            new_env.remove(e)
            new_env+=crack(e)

            # temp = arr.copy()
            # temp.append(list(new_env))

            rec(new_env, n-1, curr_ct+(len(new_env) == 1), p/M)#, list(temp))

Env = [2, 3, 4, 5]
rec(Env)
print(avg, ': ', time.time()-start_time, 'secs')