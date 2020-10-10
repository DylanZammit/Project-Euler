#A = (-340,495)
#B = (-153,-910)
#C = (835,-947)

triangles = []
with open('../p102_triangles.txt', 'r') as openfileobject:
    
    for line in openfileobject:
        pts = []
        line = [int(x) for x in line.split(',')]
        pts.append((line[0], line[1]))
        pts.append((line[2], line[3]))
        pts.append((line[4], line[5]))
        triangles.append(pts)


#pts = [A, B, C]

def get_eqn(A, B, C):
    if A[0]!=B[0]:
        m=(A[1]-B[1])/(A[0]-B[0])
        c=A[1]-m*A[0]

        ineq = 'l' if C[1] < m*C[0]+c else 'g'
    else:
        c=A[0]
        ineq = 'l' if C[0] < c else 'g'
        m='inf'

    return m, c, ineq

def is_contained(lines):
    
    for line in lines:
        (m, c, ineq) = line
        if ineq == 'l' and 0 > c or ineq == 'g' and 0 < c:
            return False
    return True

lines = []
out=0
for pts in triangles:
    lines = []
    for i in range(len(pts)):
        t = i+1 if i+1 < len(pts) else 0
        p = t+1 if t+1 < len(pts) else 0

        lines.append(get_eqn(pts[i], pts[t], pts[p]))

    if is_contained(lines): out+=1

print(out)