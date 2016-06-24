

import math as ma
import numpy as np
from random import random
import matplotlib.pyplot as plt
state = []
t=0
t_all=[]

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
 
def average_T(T):
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

def average_E(T):
    t=0

    E_average_all=[]
    E_averageT=0
    while t<=1000:
        E_total=0
        for i in range(20):   
            for j in range(20):
                de=du(i,j,state)
                E_total+=-de/2

                if de<=0.:
                      state[i][j]=-state[i][j]
                elif random()<ma.exp(-de/T):
                      state[i][j]=-state[i][j]
        t+=dt
        t_all.append(t)
        E_average=E_total/800
        E_average_all.append(E_average)
        E_averageT+=E_average
    return (E_averageT/1000.)
Tem=np.linspace(1,5,50)
E_average_=[]
T_all=[]
mag_idea_all=[]
E_average_all=[]

for T in Tem:
    T_all.append(T)
    E_average=average_E(T)
    E_average_.append(E_average)





plt.figure()
plt.plot(T_all,E_average_,'mo-',label='Energy versus Temperature')
#plt.plot(x,y,'k--')
#plt.plot(T_all,mag_idea_all,'-',label='exact result')
plt.grid(True)
plt.title('Ising model Monte Carlo')
plt.xlabel('Temperature(K)')
plt.ylabel('Energy per spin')
plt.legend(loc='upper left',frameon=False)
#plt.xlim(0,5)
#plt.ylim(-2,0)





plt.show()
   






