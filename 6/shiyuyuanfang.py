import numpy as np
import math
import matplotlib.pyplot as plt

    
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
yuanfang_all=[]
angles =np.linspace(0,np.pi/2,100)
for i in angles :
    yuanfang=with_airdrag_airdensity(i)[0][-1]
    yuanfang_all.append(yuanfang)
plt.figure()
plt.plot(angles,yuanfang_all,'k-')
plt.grid(True)

plt.title('angle and range')
plt.xlabel('angle')
plt.xticks([0,np.pi/4,np.pi/2],[r'$0$',r'$+\pi/4$',r'$+\pi/2$'])
plt.ylabel('yuanfang/m')
plt.ylim(0,30000)

plt.show()














