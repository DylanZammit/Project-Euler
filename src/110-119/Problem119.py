import numpy as np

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

nums = []

for s in range(2, 1000):
    for k in range(1, 30):
        a=s**k
        if sum_digits(a)==s:
            if a >= 10:
                nums.append(a)
nums = np.sort(nums)

M=30

print(nums[M-1])