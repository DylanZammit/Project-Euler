from math import sqrt
from numpy import gcd

def pythagoreanTriplets(M) : 
    c, m = 0, 2
    
    ans=0
    a,b=0,0

    while min(a,b) <= 3*M/2:
          
        for n in range(1, m): 
            if(gcd(m, n)==1 and (m%2==0 or n%2==0)):
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
    
                if min(a, b) > 3*M/2:
                    break 
                
                k=1
                while min(k*a, k*b)<=M:
                    ans+=count_sols(k*a, k*b, k*c, M)
                    k+=1
  
        m+=1

    return ans

def is_smallest(i, j, k, c):
    d1=sqrt((i+j)**2+k**2)
    d2=sqrt((i+k)**2+j**2)
    d3=sqrt((k+j)**2+i**2)
    
    shortest = min([d1, d2, d3])
    
    return c==shortest

def count_sols(a, b, c, M):
    out = 0

    z1=a//2
    z2=b//2

    if(b<=M and z1+1<=M):
        for i in range(1, z1+1):
            if is_smallest(a-i, b, i, c) and a-i<=M and i<=M:
                out+=1
    
    if(a<=M and z2+1<=M):
        for i in range(1, z2+1):
            if is_smallest(a, b-i, i, c) and b-i<=M and i<=M:
                out+=1
                
    return out

#M=99 : 1975
#M=100: 2060
M=1818
#1817: 999840
#1818: 1000447


#perform binary search
print(pythagoreanTriplets(M))