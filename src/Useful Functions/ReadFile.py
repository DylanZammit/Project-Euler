matrix = []

with open('../p081_matrix.txt', 'r') as openfileobject:
    for line in openfileobject:
        matrix.append([int(x) for x in line.split(',')])