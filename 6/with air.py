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



    return (x,y)
    
def with_airdrag_airdensity  (angle):



    x=[0.0]
    y=[0.0]
    vx=[700.0*np.cos(angle)]
    vy=[700.0*np.sin(angle)]
    v=[700.0]
    dt=0.02
    B2=4.0*pow(10.0,-5.0)
    at0=6.5*pow(10.0,-3.0)/280.0
    g=9.8
    alpha=2.5



    while y[-1]>=0:
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] - B2*pow(1-at0*y[-1],alpha)*v[-1]*vx[-1]*dt
        vy_new = vy[-1] - B2*pow(1-at0*y[-1],alpha)*v[-1]*vy[-1]*dt - g*dt
        v_new = math.sqrt(vx_new**2 + vy_new**2) 
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
        v.append(v_new)


    r = -float(y[-2]/y[-1])
    xl = (x[-2]+r*x[-1])/(r+1)
    yl=0
    x[-1] = xl
    y[-1] = yl



    return (x,y)
    
# plot


x1,y1 = np.array(with_airdrag_airdensity(np.pi/3))
x2,y2 = np.array(with_airdrag_airdensity(np.pi/4))
x3,y3 = np.array(with_airdrag_airdensity(np.pi*5/18))
x4,y4 = np.array(with_airdrag_airdensity(np.pi*2/9))
x5,y5 = np.array(with_airdrag_airdensity(np.pi/6))
plt.figure
ax0=plt.plot(x1,y1,'y-',label='with air 60 degree')
ax1=plt.plot(x3,y3,'r-',label='with air 50 degree')
ax2=plt.plot(x2,y2,'b-',label='with air 45 degree')
ax3=plt.plot(x4,y4,'g-',label='with air 40 degree')
ax4=plt.plot(x5,y5,'k-',label='with air 30 degree')
plt.grid(True)
plt.title('with air')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.xlim(0,51000)
plt.ylim(0,13000)

plt.legend(loc='upper right',frameon=False)

plt.show()








