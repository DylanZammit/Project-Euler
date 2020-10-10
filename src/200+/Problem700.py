import time

start_time = time.time()

p = 4503599627370517
a = 1504170715041707

# p=29
# a=11

z = pow(a, p-2, p)
n=z

B = 42298633

smallest = z+1


out = 0

i=1
while n!=1:
    n = (i*z)%p
    if n < smallest:
        print(n, i)
        out+=i
        if n == B: break
        smallest = n
    i+=1

print('-------')
smallest = p+1
n=1
while z != 1:
    z=(a*n)%p
    if z < smallest:
        print(n, z)
        if n==B: break
        out+=z
        smallest = z
    n+=1
print(time.time()-start_time, 'secs: ', out)

