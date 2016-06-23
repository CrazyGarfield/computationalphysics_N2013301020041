# -*- coding: utf-8 -*-

"""
Created on Fri Jun 8 11:33:19 2016

@author: crazygarfield   lwj
"""
#Jacobi method 
#两平板间电势
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

start = time.clock()

space = []
L=61
miao=[]
for i in range(61):   
    a=[]
    for j in range(61):
        if i == 0 or i == 60 or j == 0 or j == 60:
            voltage = 0
        elif 20<=i<=40 and j == 20:
            voltage = 1
        elif 20<=i<=40 and j == 40:
            voltage = -1
        else:
            voltage = 0
        a.append(voltage)
    space.append(a)
    miao=space
def update_v(space):

    dV = 0

    for i in range(61):    
        for j in range(61):
            if i == 0 or i == 60 or j == 0 or j == 60:
                pass
            elif 20<=i<=40 and j == 20:
                pass
            elif 20<=i<=40 and j == 40:
                pass
            else:
                voltage_new = (space[i+1][j]+space[i-1][j]+space[i][j+1]+space[i][j-1])/4
                voltage_old = space[i][j]
                dV += abs(voltage_new - voltage_old)
                miao[i][j] = voltage_new
    space=miao
    return space, dV
def Laplace_calculate(space):

    limit = 10**(-5)*61**2
    space_init = space
    
    cycle =0 
    dV=0
    while dV >= limit or cycle <= 10:
        diyici, dV = update_v(space_init)
        dierci, dV = update_v(diyici)
        space =dierci 
        cycle += 1
    print cycle    
    return dierci

end = time.clock()
print "read: %f s" % (end - start)
    

    


x = np.linspace(-1,1,61)
y = np.linspace(-1,1,61)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(space)
#画图

plt.figure()
CS = plt.contour(X,Y, Z,100)
plt.clabel(CS, inline=5, fontsize=12)
plt.title('voltage near capacitor')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

fig=plt.figure()
ax=Axes3D(fig)
a=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='jet')
fig.colorbar(a, shrink=0.5, aspect=5)
ax.set_title('voltage near capacitor')
ax.set_xlabel('x(m)');ax.set_ylabel('y(m)');ax.set_zlabel('Potential(V)')

plt.figure()
CS = plt.contour(X,Y, Z,25)
plt.clabel(CS, inline=1)
plt.title('voltage near capacitor')
plt.xlabel('x(m)')
plt.ylabel('y(m)')



plt.show()
    

 

