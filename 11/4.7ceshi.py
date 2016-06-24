import numpy
import math
import pickle
from pylab import *

x1=1
y1=0
x2=0
y2=0
vx1=0
vx2=0
pi=3.141592653
vy1=2.00005
vy2=0

t=0
dt=0.000001
r=0
#vy1=float(raw_input())
#vy2=float(raw_input())
#vx1=float(raw_input())

x1_all=[]
y1_all=[]
x2_all=[]
y2_all=[]
r_all=[]
t_all=[]
a=0.1

while(t<30):
        x1_all.append(x1)
        y1_all.append(y1)
        x2_all.append(x2)
        y2_all.append(y2)
        r_all.append(t)
        t_all.append(r)

        r=sqrt((x1-x2)**2+(y1-y2)**2)
        vx1=vx1-(dt*a*4*x1*pi**2)/(r**3)
        x1=x1+vx1*dt
        vy1=vy1-(dt*a*4*y1*pi**2)/(r**3)
        y1=y1+vy1*dt
        vx2=vx2-(dt*x2*4*pi**2)/(r**3)
        x2=x2+vx2*dt
        vy2=vy2-(dt*y2*4*pi**2)/(r**3)
        y2=y2+vy2*dt
        t=t+dt



figure2=plt.figure('b')
plot(x1_all,y1_all)
plot(x2_all,y2_all)
figure1=plt.figure('a')
fig2=plot(r_all,t_all)
show()

