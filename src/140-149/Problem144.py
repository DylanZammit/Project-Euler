from math import *
from numpy.linalg import norm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from time import sleep

a=5
b=10

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)

axes()
plt.contour(x, y,(x**2/a**2 + y**2/b**2), [1], colors='k')

m1=(10.1--9.6)/-1.4

p = (1.4, -9.6)

plt.plot([0, p[0]], [10.1, p[1]], color='r')
plt.draw()
plt.pause(0.01)

count = 0
while(not(-0.01 <= p[0] <= 0.01 and p[1] > 0)):
    m = -4*p[0]/p[1]
    m1 = ((2 * m) + (m1 * m**2) - m1) / (2 * m * m1 - m**2 + 1)

    c = p[1]-m1*p[0]

    x = np.roots([a**2*m1**2+b**2, 2*a**2*m1*c, a**2*(c**2-b**2)])
    y = [m1*v+c for v in x]
    
    p_old = p
    
    p = (x[1], y[1]) if norm((x[0]-p[0], y[0]-p[1])) < norm((x[1]-p[0], y[1]-p[1])) else (x[0], y[0])

    
    plt.plot([p_old[0], p[0]], [p_old[1], p[1]], color='r')
    plt.draw()
    plt.pause(0.1)
    count+=1

plt.show()

print(count)