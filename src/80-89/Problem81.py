import numpy as np

matrix = []

with open('../p081_matrix.txt', 'r') as openfileobject:
    for line in openfileobject:
        matrix.append([int(x) for x in line.split(',')])
n = len(matrix)

max_val = max([max(x) for x in matrix])

for i in range(1, 2*n):
    
    y, x = (n-i-1, n-1) if i < n else (0, 2*n-i-2)
    
    while 0 <= x < n and 0 <= y < n:
        val_right = matrix[y][x+1] if x+1 < n else max_val**5
        val_down = matrix[y+1][x] if y+1 < n else max_val**5

        matrix[y][x] += min(val_right, val_down)
        
        y, x = y+1, x-1
        

print(matrix[0][0])