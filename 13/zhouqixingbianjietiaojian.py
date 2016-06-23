# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 8 20:27:50 2016

@author: lwj
"""



#Jacobi method 
#两平板间电势
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



space = []

for i in range(61):   
    a=[]
    for j in range(61):
        if i == 0 or i == 60 or j == 0 or j == 60:
            voltage = 0
        elif 20<=i<=40 and j == 20:
            voltage =  1
        elif 20<=i<=40 and j == 40:
            voltage = -1
        else:
            voltage = 0
        a.append(voltage)
    space.append(a)

def du(space):
    m=60
    dV=0
    for i in range(61):
        for j in range(61):
            if i==0:
                top=space[m][j]
            else:
                top=space[i-1][j]
            if i==m:
                down=space[0][j]
            else:   
                down=space[i+1][j]
            if j==0:
                left=space[i][m]
            else :
                left=space[i][j-1]
            if j==m:
                right=space[i][0]
            else :
                right=space[i][j+1]
                if 20<=i<=40 and j == 20:
                    space[i][j]=space[i][j]
                elif 20<=i<=40 and j == 40:
                    space[i][j]=space[i][j]
                else:
                
                    voltage_new = (top+down+left+right)/4.
                    voltage_old = space[i][j]
                    dV += abs(voltage_new - voltage_old)
                    space[i][j] = voltage_new
    return space, dV
def Laplace_calculate(space):

    limit = 10**(-5)*61**2
    space_init = space
    
    cycle =0 
    dV=0
    while dV >= limit or cycle <= 100:
        diyici, dV = du(space_init)
        dierci, dV = du(diyici)
        space =dierci 
        cycle += 1
    print cycle    
    return dierci

    


x = np.linspace(-1,1,61)
y = np.linspace(-1,1,61)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(space)

plt.figure()
CS = plt.contour(X,Y, Z,10)
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
    
#x = linspace(-1.75, 1.75, 101)
#y = linspace(-1.75, 1.75, 101)


#X,Y = meshgrid(x,y)
#z=a
#plt.figure()
#CS = plt.contour(x, y, z)
 

