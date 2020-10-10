import numpy as np

triangle = []

with open('../p067_triangle.txt', 'r') as openfileobject:
    for line in openfileobject:
        triangle.append([int(x) for x in line.split()])

for row_num in range(len(triangle)-2, -1, -1):

    for idx in range(len(triangle[row_num])):
        triangle[row_num][idx] = triangle[row_num][idx] + max(triangle[row_num+1][idx], triangle[row_num+1][idx+1])

print(triangle[0][0])

