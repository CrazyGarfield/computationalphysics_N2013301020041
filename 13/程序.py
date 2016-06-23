
"""
Created on Sat Jun 8 21:30:43 2016

@author:  crazyGarfield lwj
"""

#Jacobi method 

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

start = time.clock()

miao=[]
N_all=[]
L_all=[]
NSOR_all=[]
LSOR_all=[]

 #SOR menthod   
def update_SOR(space,L):
    
    dV = 0

    for i in range(L):    
        for j in range(L):
            if i == 0 or i == L-1 or j == 0 or j == L-1:
                pass
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(20/61)):
                pass
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(40/61)):
                pass
            else:
                voltage_new = (space[i-1][j]+space[i+1][j]+space[i][j-1]+space[i][j+1])/4.
                voltage_old = space[i][j]
                dVla = voltage_new - voltage_old
                alpha = 2/(1+(np.pi/L))
                voltage_new = alpha*dVla + voltage_old
                dV += abs(voltage_new - voltage_old)
                space[i][j] = voltage_new

    return space, dV

def SOR(L):
    space=[]
    
    for i in range(L):   
        a=[]
        for j in range(L):
            if i == 0 or i == L-1 or j == 0 or j == L-1:
                voltage = 0
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(20/61)):
                voltage = 1
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(40/61)):
                voltage = -1
            else:
                voltage = 0
            a.append(voltage)
        space.append(a)
        

    limit = 10**(-5)*L**2
    space_init = space
    
    cycle =0 
    dV=0
    while dV >= limit or cycle <= 3:
        diyici, dV = update_SOR(space_init,L)
        dierci, dV = update_SOR(diyici,L)
        space_init =dierci 
        cycle += 1
    print cycle    
    return cycle
#Jacobi method
def update_vJ(space,L):
    miao=space
    dV = 0

    for i in range(L):    
        for j in range(L):
            if i == 0 or i == L-1 or j == 0 or j == L-1:
                pass
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(20/61)):
                pass
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(40/61)):
                pass
            else:
                voltage_new = (space[i-1][j]+space[i+1][j]+space[i][j-1]+space[i][j+1])/4.
                voltage_old = space[i][j]
                dV += abs(voltage_new - voltage_old)
                miao[i][j] = voltage_new
    space=miao
    return space, dV

def Jacobi(L):
    space=[]
    
    for i in range(L):   
        a=[]
        for j in range(L):
            if i == 0 or i == L-1 or j == 0 or j == L-1:
                voltage = 0
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(20/61)):
                voltage = 1
            elif int(L*(20/61))<=i<=int(L*(40/61)) and j == int(L*(40/61)):
                voltage = -1
            else:
                voltage = 0
            a.append(voltage)
        space.append(a)
        

    limit = 10**(-5)*L**2
    space_init = space
    
    cycle =0 
    dV=0
    while dV >= limit or cycle <= 10:
        diyici, dV = update_vJ(space_init,L)
        dierci, dV = update_vJ(diyici,L)
        space_init =dierci 
        cycle += 1
    print cycle    
    return cycle

end = time.clock()
print "read: %f s" % (end - start)



for i in range(61):
    L_all.append(9+i)
    N_all.append(Jacobi(9+i))
    LSOR_all.append(9+i)
    NSOR_all.append(SOR(9+i))
plt.plot(L_all,N_all,'yo-',label='Jacobi method')
plt.plot(LSOR_all,NSOR_all,'r.-',label='SOR method')
plt.legend()
plt.grid(True)
plt.xlabel('L(m)')
plt.ylabel('Number of iteration ')
plt.title('Number of iteration with different L')
plt.show()





