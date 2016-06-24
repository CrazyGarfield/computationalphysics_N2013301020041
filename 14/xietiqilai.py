from __future__ import division
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from copy import copy

fig = plt.figure()
ax = fig.add_subplot(1,1,1,xlim=(0,1),ylim=(-1,1))
line, = ax.plot([],[],lw=2)
def init(): 
    line.set_data([], []) 
    return line,


def animate(i):
 
    x = np.linspace(0,1,101)
    y_now=copy(x)
    for d in range(101):
        
        if 0<=d<=25:
            y_now[d]= 2*x[d]
        else:
            y_now[d]= -(2/3)*x[d]+2/3
    y_before =copy( y_now)
    y_after = np.zeros(101)

    for j in range(i):
        for i in range(101):
                if i== 0 or i== 100:
                    y_after[i] = 0
                else:
                    y_after[i] =  y_now[i+1] - y_before[i] + y_now[i-1]

        y_before = copy(y_now)
        y_now = copy(y_after)
    y=y_now
    line.set_data(x,y)
    return line,

    


ani = animation.FuncAnimation(fig, animate,init_func=init,  interval=10) 
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title('wave on a string')
plt.grid(True)
plt.show()
    
                    

    
    
    
    
    





