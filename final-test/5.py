
import math as ma
import numpy as np
from random import random
import matplotlib.pyplot as plt
state = []
t=0
t_all=[]


dt=1
mag_all=[]
for i in range(20):   
    a=[]
    for j in range(20):
        spin=1
        a.append(spin)
    state.append(a)



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
 



t=0
E_total=0
E_averageall1=[]
E_averageall2=[]
T1=1.5  
T2=2.0
T3=2.25
T4=4.0

while t<1000:
    t_all.append(t)
    
    E_total=0
        
    for i in range(20):   
        for j in range(20):
            de=du(i,j,state)
            E_total+=-de/2
            
            if de<=0.:
                state[i][j]=-state[i][j]
            elif random()<ma.exp(-de/T1):
                state[i][j]=-state[i][j]
    t+=dt
    E_averageall1.append(E_total/800.)



plt.plot(np.array(t_all),np.array(E_averageall1),label='T=1.5')
plt.title('Ising model Energy vs. Time')
plt.xlabel('Time')
plt.ylabel('Energy')
plt.legend(loc='upper left',frameon=False)
plt.ylim(-2,0)    
"""
plt.figure(2)
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)

plt.sca(ax1)
plt.plot(np.array(t_all),np.array(E_averageall1),label='')
plt.title('Ising model Energy vs. Time')
plt.xlabel('')
plt.ylabel('Energy')
plt.legend(loc='upper left',frameon=False)
plt.ylim(-2,0)

plt.sca(ax2)
plt.plot(np.array(t_all),np.array(E_averageall2),label='')
plt.title('Ising model Energy vs. Time')
plt.xlabel('')
plt.ylabel('')
plt.legend(loc='upper left',frameon=False)
plt.ylim(-2,0)

plt.sca(ax2)
plt.plot(np.array(t_all),np.array(E_averageall),label='')
plt.title('Ising model Energy vs. Time')
plt.xlabel('')
plt.ylabel('')
plt.legend(loc='upper left',frameon=False)
plt.ylim(-2,0)

plt.sca(ax2)
plt.plot(np.array(t_all),np.array(E_averageall),label='')
plt.title('Ising model Energy vs. Time')
plt.xlabel('')
plt.ylabel('')
plt.legend(loc='upper left',frameon=False)
plt.ylim(-2,0)
"""
plt.show()