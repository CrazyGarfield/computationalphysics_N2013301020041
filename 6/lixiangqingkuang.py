import numpy as np
import math
import matplotlib.pyplot as plt
# initial

def initial(angle):

    

    x=[0.0]
    y=[0.0]
    vx=[700.0*np.cos(angle)]
    vy=[700.0*np.sin(angle)]
    v=[700.0]
    dt=0.02

    g=9.8



    while y[-1]>=0:
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] 
        vy_new = vy[-1] - g*dt
        v_new = math.sqrt(vx_new**2 + vy_new**2) 
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
        v.append(v_new)

#the landing point

    r = -float(y[-2]/y[-1])
    xl = (x[-2]+r*x[-1])/(r+1)
    yl=0
    x[-1] = xl
    y[-1] = yl

    # result

    return (x,y)

# plot


x1,y1 = np.array(initial(np.pi/4))


plt.figure
ax0=plt.plot(x1,y1,'y-',label='45 degree')



plt.grid(True)
plt.title('ideal')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.xlim(0,51000)
plt.ylim(0,13000)

plt.legend(loc='upper right',frameon=False)

plt.show()




