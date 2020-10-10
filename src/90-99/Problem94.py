# from math import sqrt
# from matplotlib import pyplot as plt

# B=10**9
# M=(B+1)//3+1

# def is_area_integral(a, b): 
#     V = b*sqrt(a**2-b**2/4)/2
#     return V==int(V)

# #case: 1, 1, 2
# ans=4

# sides=[1]

# # for a in range(2, M):
# for a in range(2, 100000):
#     if(is_area_integral(a, a+1) and 3*a+1<=B): 
#         print(a, a, a+1, 'A')
#         sides.append(a)
#         ans+=3*a+1
#     if(is_area_integral(a, a-1) and 3*a-1<=B): 
#         print(a, a, a-1, 'B')
#         sides.append(a)
#         ans+=3*a-1
#     if(a%1000000==0): print(a)
# print(ans)

# print(sides)

from numpy import gcd

M=10**9
ans=0

def pythagoreanTriplets(M) : 
    c, m = 0, 2
    
    ans=0
    a,b=0,0

    while 2*b+2*c <= M and 2*a+2*c <= M:
          
        for n in range(1, m): 
            if(gcd(m, n)==1 and (m%2==0 or n%2==0)):
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
            
                if(c==2*b+1 or c==2*b-1):
                    ans+=2*(b+c)
                if(c==2*a+1 or c==2*a-1):
                    ans+=2*(a+c)
        m+=1
    return ans
print(pythagoreanTriplets(M))
    