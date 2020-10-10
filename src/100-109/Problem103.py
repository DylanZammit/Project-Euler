from itertools import combinations

def get_near_opt(A):
    ind = len(A)//2
    b = A[ind]
    return [b]+[ b+a for a in A ]

def S(A): return sum(A)

def is_special(A):
    
    for r in range(1, len(A)-1):
        for subset in combinations(range(len(A)), r):
            B = [A[i] for i in subset]

            rem_ind = set(range(len(A))).difference(set(subset))

            C = [A[i] for i in rem_ind]

            if len(B) == len(C) and S(B) == S(C): return False
            if len(B) < len(C) and S(B) >= S(C) or len(B) > len(C) and S(B) <= S(C): return False
    return True


# A = [11, 17, 20, 22, 23, 24]
# # print(is_special(A))
# print(get_near_opt(A))
A = [11, 18, 19, 20, 22, 25]
# print(is_special(A))
# print(get_near_opt(A))
A=[20, 31, 38, 39, 40, 42, 45]
print(S(A))
B = [19, 21, 22, 23, 24, 25, 26]
print(is_special(B))
print(S(B))


