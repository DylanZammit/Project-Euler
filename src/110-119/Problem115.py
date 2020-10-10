def f(n): return (n+1)*(n-4)//2+3
def f(n, m): return (n+1)*(n-m+1)-(n*(n+1)-m*(m-1))//2

def F(m,n, stick = {}):
    ans = f(n,m)

    for z in range(m, n-(m+1)+2):

        for j in range(m, z):

            if str(j) not in stick:
                stick[str(j)]=F(m,j, stick)
            
            ans+=stick[str(j)]

    return ans
    
m=50
n=51
while F(m, n)+1 < 1000000:
    n+=1
print(n)