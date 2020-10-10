stick = {}

def f(n): return (n+1)*(n-4)//2+3

def find_comb(n):
    ans = f(n)

    for z in range(3, n-4+2):

        for j in range(3, z):

            if str(j) not in stick:
                stick[str(j)]=find_comb(j)
            
            ans+=stick[str(j)]

    return ans

print(find_comb(50)+1)