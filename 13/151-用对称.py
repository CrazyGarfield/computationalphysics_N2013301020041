# -*- coding: utf-8 -*-
"""
Created on Jun 8 13:05:33 2016

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
Z0=[]
for i in range(151):   
    a=[]
    for j in range(151):
        if i == 0 or i == 150 or j == 0 or j == 150:
            voltage = 0
        elif 50<=i<=100 and j == 50:
            voltage = 1
        elif 50<=i<=100 and j == 100:
            voltage = -1
        else:
            voltage = 0
        a.append(voltage)
    space.append(a)
  
def update_v(space):

    dV = 0

    for i in range(76):    
        for j in range(76):
            if i == 0 or j == 0 :
                pass
            elif 50<=i<=75 and j == 50:
                pass

            elif i==75 and j!=50 :
                voltage_new = (space[i-1][j]+space[i-1][j]+space[i][j+1]+space[i][j-1])/4
                voltage_old = space[i][j]
                dV += abs(voltage_new - voltage_old)
                space[i][j] = voltage_new 
            else:
                voltage_new = (space[i+1][j]+space[i-1][j]+space[i][j+1]+space[i][j-1])/4
                voltage_old = space[i][j]
                dV += abs(voltage_new - voltage_old)
                space[i][j] = voltage_new

    return space, dV
    
def Laplace_calculate(space):

    limit = 10**(-5)*151**2
    space_init = space
    
    cycle =0 
    dV=0
    while dV >= limit or cycle <= 10:
        diyici, dV = update_v(space_init)
        dierci, dV = update_v(diyici)
        space_init =dierci 
        cycle += 1
    print cycle    
    return space

end = time.clock()
print "read: %f s" % (end - start)
Z0=Laplace_calculate(space)  
def transform(Z0):
    for i in range(151):    
        for j in range(151):
            if i == 0 or i == 150 or j == 0 or j == 150:
                pass
            elif 0<=i<=75 and 0<=j<=75 :
                pass
            elif 75<i<=150 and 75<=j<=150:
                Z0[i][j]=Z0[i-(i-75)*2][j]
            elif 0<=i<=75 and 75<=j<=150:
                Z0[i][j]=-Z0[i][j-(j-75)*2]
            else:
                Z0[i][j]=-Z0[i-(i-75)*2][j-(j-75)*2]
    return Z0
  


x = np.linspace(-1,1,151)
y = np.linspace(-1,1,151)
X, Y = np.meshgrid(x, y)
Z=transform(Z0)

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
    

 
