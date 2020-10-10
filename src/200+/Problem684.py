def fibonacci(n):
    fn = [0, 1]
    for i in range(2, n+1):
        fn.append(fn[i-1] + fn[i-2])
    return fn


def S(x, m): 
    a=x//9
    b=x%9
    return int(pow(10, a, m)*(6+b+int(b*(b+1)/2))-9*a-6-b)

fn = fibonacci(90)
fn = fn[2:]

m=1000000007
ans = int(0)
for f in fn:
    ans+=S(f, m)

print(ans%m)
