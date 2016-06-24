
import math as ma
import numpy as np

from random import random
import matplotlib.pyplot as plt
state = []
t=0
t_all=[]
T=4.0
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
      mag_all.append(mag)
plt.plot(np.array(t_all),np.array(mag_all),label='T=4.0')
plt.title('Ising model Magnetization vs. Time')
plt.xlabel('Time')
plt.ylabel(' Magnetization')
plt.legend(loc='down right',frameon=False)
plt.ylim(-1,1.2)   
#print"total simulation time is %g seconds of tempreture%g K"%(dt,T)