U = 45

digits = list(range(2, U+1))
digits.reverse()

count = 0

N = len(digits)

#set smallest possible?
eps = 10**(-20)

def get_ans(rem=1/2, ind = 0, arr=[]):
    global count
    if ind < N and 1/digits[ind]**2<rem:
        if abs(rem)<eps:
            count+=1
            print(arr)
            print(sum(1/d**2 for d in arr))
        elif rem > 0:
            for i in range(ind, N):
                d=digits[i]
                get_ans(rem-1/d**2, i+1, arr+[d])
get_ans()
print(count)
