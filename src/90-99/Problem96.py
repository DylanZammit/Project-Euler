import numpy as np

def check_row(A, i, j):
    
    illeg=[]
    for n in range(9):
        a = A[i, n]
        if n!=j and a!=0:
            illeg.append(a)

    return illeg

def check_col(A, i, j):
    illeg=[]
    for n in range(9):
        a = A[n, j]
        if n!=i and a!=0:
            illeg.append(a)
    return illeg

def check_3x3(A, i, j):
    u_0 = (i//3)*3
    v_0 = (j//3)*3
    illeg=[]

    for u in range(u_0, u_0+3):
        for v in range(v_0, v_0+3):
            a = A[u, v]
            if((u!=i or v!=j) and a!=0):
                illeg.append(a)
    return illeg

def update_possibilities(A, i, j):
    if A[i,j] == 0:
        out = check_col(A, i, j)
        out += check_row(A, i, j)
        out += check_3x3(A, i, j)

        temp = []

        for k in range(1, 10):
            if(k not in out): temp.append(k)
        out = temp
        out = list(set(out))
        return out
    else:
        return []
        
def check_trivial(A):
    for i in range(9):
        for j in range(9):
            p=update_possibilities(A, i, j)
            if len(p)==1:
                A[i, j] = p[0]
            elif len(p)==0 and A[i,j] == 0:
                return A, True
    return A, False

def guess(A):
    for i in range(9):
        for j in range(9):
            poss = update_possibilities(A, i, j)
            if(len(poss) > 0):
                k=0
                boo = True
                while k < len(poss) and boo:
                    B=A.copy()
                    B[i, j] = poss[k]
                    B, boo = solve(B)
                    if(not boo): 
                        return B, boo
                    k+=1
                return B, True
    return A, False
                    
def solve(A):

    while np.any(A==0):

        A, boo = check_trivial(A)
        if(boo): return A, boo
        A, boo = guess(A)
        if(boo): return A, boo
    return A, False

with open('../p096_sudoku.txt', 'r') as openfileobject:

    ans = 0
    matrix=[]

    for line in openfileobject:
        if line[0]!='G':
            line = line.replace('\n','')
            matrix.append([int(x) for x in line])

        if(len(matrix) == 9):
            A, boo = solve(np.matrix(matrix))
            ans+=(A[0,0]*100+A[0, 1]*10+A[0,2])
            matrix=[]

print(ans)