S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
D = [2*z for z in S]
T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
T = [3*z for z in T]

out=0

def f(score, throws_left, last_type=0, ilt=0):
    global out
    if throws_left == 0 and score == 0 or score==0:
        out+=1
    elif throws_left > 0 and score >= 1:
        throws_left-=1
        if last_type == 0:
            for i in range(ilt, len(S)):
                f(score-S[i], throws_left, 0, i)
            for i in range(len(D)):
                f(score-D[i], throws_left, 1, i)
            for i in range(len(T)):
                f(score-T[i], throws_left, 2, i)
        if last_type == 1:
            for i in range(ilt, len(D)):
                f(score-D[i], throws_left, 1, i)
            for i in range(len(T)):
                f(score-T[i], throws_left, 2, i)
        if last_type == 2:
            for i in range(ilt, len(T)):
                f(score-T[i], throws_left, 2, i)

def get_throw(score):
    for d in D:
        f(score-d, 2)
M=99
for score in range(1, M+1):
    get_throw(score)
print(out)