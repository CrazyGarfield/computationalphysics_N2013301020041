

import math as ma
import numpy as np
from random import random
import matplotlib.pyplot as plt
state = []
t=0
t_all=[]
T=1.5
sum=0
dt=1
mag_all=[]
for i in range(20):   
    a=[]
    for j in range(20):
        spin=1
        a.append(spin)
    state.append(a)


def M(i,j,state,sum):
  
        for i in range(20):   
            for j in range(20):
                sum=1.*state[i][j]+sum
        return sum/400.
def du(i,j,state):
	m=19
	if i==0:
		top=state[m][j]
	else:
		top=state[i-1][j]
	if i==m:
		down=state[0][j]
	else:   
		down=state[i+1][j]
	if j==0:
		left=state[i][m]
	else :
		left=state[i][j-1]
	if j==m:
		right=state[i][0]
	else :
		right=state[i][j+1]
	return 2.*state[i][j]*(top+down+left+right)
 
def average(T):
    t=0
    mag_total=0
    while t<1000:
        for i in range(20):   
            for j in range(20):
                de=du(i,j,state)
                if de<=0.:
                      state[i][j]=-state[i][j]
                elif random()<ma.exp(-de/T):
                      state[i][j]=-state[i][j]
        t+=dt
        t_all.append(t)
        mag=M(i,j,state,sum)
        mag_total+=mag
    return mag_total/1000.

Tem=np.linspace(1,5,50)
mag_average_all=[]
T_all=[]
mag_idea_all=[]
for T in Tem:
    mag_average=average(T)
    mag_average_all.append(mag_average)
    T_all.append(T)
    #analytic
    mag_idea=(2.27-T)**(1/8)
    mag_idea_all.append(mag_idea)
x=np.linspace(0,5,50)    
y=np.linspace(0,0,50)
plt.figure()
plt.plot(T_all,mag_average_all,'mo-',label='Monte Carlo result')
#plt.plot(x,y,'k--')
#plt.plot(T_all,mag_idea_all,'-',label='exact result')
plt.grid(True)
plt.title('Ising model Monte Carlo')
plt.xlabel('Temperature(K)')
plt.ylabel('Magnetization')




plt.legend(loc='upper right',frameon=False)
plt.xlim(0,5)
plt.show()
   




