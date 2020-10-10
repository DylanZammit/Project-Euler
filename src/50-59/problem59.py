import numpy as np

nums = []

with open('../p059_cipher.txt', 'r') as openfileobject:
    for line in openfileobject:
        nums.append([int(x) for x in line.split(',')])

nums = nums[0]

out = 0

for i in range(len(nums)):
    vals = nums[i]
    if i%3==0:
        print(chr(vals^103), end ="")
        out+=vals^103
    elif i%3==1:
        print(chr(vals^111), end ="")
        out+=vals^111
    else:
        print(chr(vals^100), end ="")
        out+=vals^100

print(out)