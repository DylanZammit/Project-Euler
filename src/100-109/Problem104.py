import collections
import math
import time
start_time = time.time()

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

x0=1
x1=1
count = 2
found = False

def is_pan(x):
    x = [v for v in str(x)]
    digits = [str(v) for v in range(1, 10)]
    return len(x) == 9 and collections.Counter(x) == collections.Counter(digits)

while not found:
    x2=x0+x1
    x0=x1
    x1=x2

    found = is_pan(int(first_n_digits(x2, 9))) and is_pan(int(x2%(10**9)))
    if count%10000==0: print(count)
    count+=1

print(count)
print("--- %s seconds ---" % (time.time() - start_time))