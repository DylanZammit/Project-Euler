import time
start_time = time.time()

L=20
# L=10
count = 0

def get_num(arr):
    global count
    rem = L-len(arr)
    # if rem==1:
    #     count+=9-arr[-1]-arr[-2]+1
    #     return
    if rem==0:
        count+=1
        print(arr)
        return
    maxim = 9-arr[-1] if rem==L-1 else 9-arr[-1]-arr[-2]
    
    for i in range(maxim+1):
        get_num(arr+[i])

for i in range(1, 10):            
    get_num([i])
    print(i)
print(count, float(time.time()-start_time), 'secs')

# def S(n):
#     return n*(n+1)//2

# def f(n):
#     if n==2: return S(10)
#     return sum(S(i) for i in range(1, 11))*f(n-1)

# print(sum(S(i) for i in range(1, 10))*f(19))

