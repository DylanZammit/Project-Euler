import numpy as np

couples = []

with open('../p099_base_exp.txt', 'r') as openfileobject:
    for line in openfileobject:
        couples.append([int(x) for x in line.split(',')])

new_comp = []

for couple in couples:
    new_comp.append(couple[1]*np.log(couple[0]))

print(np.argmax(new_comp)+1)