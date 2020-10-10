import numpy as np
import time
start_time = time.time()

M = []

with open('../p345_matrix_sum.txt', 'r') as openfileobject:
    for line in openfileobject:
        line.replace('\n', '')
        M.append([int(x) for x in line.split(' ')])

M = [[7, 53, 183, 439, 863], 
[497, 383, 563, 79, 973], 
[287, 63, 343, 169, 583], 
[627, 343, 773, 959, 943], 
[767, 473, 103, 699, 303]]

M = np.matrix(M)

maxi = 0

def mat_sum(M, S = 0):
    global maxi
    if np.size(M)==1:

        z = S+M[0,0]
        if z > maxi:
            maxi = z
    else:

        dim = M.shape[0]

        for i in range(dim):
            T = np.delete(M, 0, axis = 0)
            T = np.delete(T, i, axis = 1)
            mat_sum(T, S+M[0, i])

mat_sum(M)
print(maxi, ': ', time.time()-start_time, 'secs')