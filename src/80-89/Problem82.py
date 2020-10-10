import numpy as np

A = []

with open('../p082_matrix.txt', 'r') as openfileobject:
    for line in openfileobject:
        A.append([int(x) for x in line.split(',')])

A = np.matrix(A)
# A = np.matrix([[131, 673, 234, 103, 18],[201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])

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
    return out

def shortest(start):
    
    B = np.ones((dims[0], dims[1]))*M
    B[start, 0]=A[start, 0]

    Q = []

    for i in range(dims[0]):
        for j in range(dims[1]):
            Q.append((i, j))
        
    while len(Q)>0:
        # if((destination, dims[1]-1) not in Q): return B[destination, dims[1]-1]


        #MORE EFFICIENT
        min_val, u = find_smallest(Q, B)
        Q.remove(u)

        neighbours = get_neighbours(u, Q)

        for v in neighbours:
            alt = B[u]+A[v]

            if alt < B[v]:
                B[v] = alt
                
    return min(B[:, dims[1]-1])

out_arr = []

for start in range(dims[0]):
    print(start)
    out_arr.append(shortest(start))
    # print(shortest(start))
print(min(out_arr))