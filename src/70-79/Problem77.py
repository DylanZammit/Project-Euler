import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


count = 0

def split_primes(x):
    primes=[2]
    n=3
    while n<=x:
        if(is_prime(n)):primes.append(n)
        n=n+2 

    rec(x, primes)

def rec(x, primes):
    global count

    if x in primes:
        count+=1

    if x > 2:
        for i in range(len(primes)):
            p=primes[i]
            if(x-p > 0):
                rec(x-p, primes[:i+1])
    
x=1
while count < 5000:
    x+=1
    count=0
    split_primes(x)
print(x)



