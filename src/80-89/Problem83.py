import numpy as np

A = []

with open('../p082_matrix.txt', 'r') as openfileobject:
    for line in openfileobject:
        A.append([int(x) for x in line.split(',')])

A = np.matrix(A)

M = np.sum(A)+1
dims = A.shape

def find_smallest(Q, B):
    min_val = M
    
    for q in Q:
        if B[q]<min_val:
            min_val = B[q]
            arg_min = q

    return min_val, arg_min

def get_neighbours(coord, Q):
    i=coord[0]
    j=coord[1]

    out=[]
    if (i+1, j) in Q:
        out.append((i+1, j))
    if (i-1, j) in Q:
        out.append((i-1, j))
    if (i, j+1) in Q:
        out.append((i, j+1))
    if (i, j-1) in Q:
        out.append((i, j-1))
    return out

def shortest():
    
    B = np.ones((dims[0], dims[1]))*M
    B[0, 0]=A[0, 0]

    Q = []

    for i in range(dims[0]):
        for j in range(dims[1]):
            Q.append((i, j))
        
    while len(Q)>0:
        if((dims[0]-1, dims[1]-1) not in Q): return B[dims[0]-1, dims[1]-1]

        #MORE EFFICIENT
        min_val, u = find_smallest(Q, B)
        Q.remove(u)

        neighbours = get_neighbours(u, Q)

        for v in neighbours:
            alt = B[u]+A[v]

            if alt < B[v]:
                B[v] = alt
                
    return B[dims[0]-1, dims[1]-1]

print(shortest())