import math

d = 12000

rationals = []

for b in range(1, d+1):
    for a in range(1, b):
        inp = a/b
        if 1/3 < inp < 1/2 and math.gcd(a, b) == 1:
            rationals.append(inp)

print(len(rationals))
