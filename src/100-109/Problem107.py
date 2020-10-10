import numpy as np

matrix = []
with open('../p107_network.txt', 'r') as openfileobject:
    for line in openfileobject:
        line=line.replace('-\n','-')
        matrix.append([int(x) if x!='-' else 0 for x in line.split(',')])
        
n=len(matrix[0])
matrix = np.matrix(matrix)

edge_weights = {}

for i in range(n):
    for j in range(i+1, n):
        edge_weights[str((i,j))]=matrix[i, j]
edge_weights = sorted(edge_weights.items(), key=lambda x: x[1])

trees = [[i] for i in range(n)]
x = 0

total = sum(v[1] for v in edge_weights)

sum_span = 0 

while len(trees)>1:
    print(trees)
    curr = edge_weights[x]
    edge = curr[0][1:-1]
    weight = curr[1]
    if weight != 0:
        [v1,v2]=[int(v) for v in edge.split(',')]

        for tree in trees:
            if v1 in tree:
                tree1 = tree
        
        for tree in trees:
            if v2 in tree:
                tree2 = tree

        if set(tree1)!=set(tree2):
            trees.remove(tree1)
            trees.remove(tree2)

            trees.append(list(set(tree1+tree2)))

            sum_span+=weight
    x+=1

print(total - sum_span)
