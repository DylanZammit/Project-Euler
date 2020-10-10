from math import sqrt

# x = blue....y = red
# x/(x+y)*(x-1)/(x+y-1)=1/2
# 2*x(x-1)=(x+y)(x+y-1)>z(z-1)=B
# 2*x(x-1) > B
# x > (1+sqrt(1+2*z))/2

def prob(x, y): return x*(x-1)/((x+y)*(x+y-1))

def get_y(x): return (sqrt(8*x**2-8*x+1)-2*x+1)/2

def is_found(x):
    y=get_y(x)
    return y==int(y), y

z=10**12

x=int((1+sqrt(1+2*z))/2)

x=15

temp = []

prev_rat=1
prev_x=14

while True:

    state, y = is_found(x)
    if(y==int(y) and x+y>z): break

    if(state):
        print(x,y)
        prev_rat=x/prev_x
        prev_x=x

        x=int(x*prev_rat)
    else:
        x+=1
print(x, y)
