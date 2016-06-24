import numpy
import math
import pickle
from pylab import *

x1=1
y1=1
x2=-0.05
y2=-0.05
x3=0.1
y3=-0.1
vx1=0
vx2=0
#pi=3.141592653
vy1=0.7
vy2=-0.7
vx3=0
vy3=0.7

dt=0.0001
r=0
ceta=0
t=0
#vy1=float(raw_input())
#vy2=float(raw_input())
#vx1=float(raw_input())

x1_all=[]
y1_all=[]
x2_all=[]
y2_all=[]
x3_all=[]
y3_all=[]
r_all=[]
t_all=[]
ceta_all=[]
a=0.1

while(t<0.1):
        x1_all.append(x1)
        y1_all.append(y1)
        x2_all.append(x2)
        y2_all.append(y2)
        x3_all.append(x3)
        y3_all.append(y3)
        r_all.append(r)
	t_all.append(t)
        ceta_all.append(ceta)
        r1=sqrt((x1-x2)**2+(y1-y2)**2)
        r2=sqrt((x1-x3)**2+(y1-y3)**2)
	r3=sqrt((x2-x3)**2+(y2-y3)**2)

        vx1=vx1-(dt*a*4*x1*pi**2)/(r1**3)-(dt*a*4*x1*pi**2)/(r2**3)-(dt*a*4*x1*pi**2)/(r3**3)
        x1=x1+vx1*dt
        vy1=vy1-(dt*a*4*y1*pi**2)/(r1**3)-(dt*a*4*y1*pi**2)/(r2**3)-(dt*a*4*y1*pi**2)/(r3**3)
        y1=y1+vy1*dt

        vx2=vx2-(dt*x2*4*pi**2)/(r1**3)-(dt*x2*4*pi**2)/(r2**3)-(dt*x2*4*pi**2)/(r3**3)
        x2=x2+vx2*dt
        vy2=vy2-(dt*y2*4*pi**2)/(r1**3)-(dt*y2*4*pi**2)/(r2**3)-(dt*y2*4*pi**2)/(r3**3)
        y2=y2+vy2*dt

        vx3=vx3-(dt*x3*4*pi**2)/(r1**3)-(dt*x3*4*pi**2)/(r2**3)-(dt*x3*4*pi**2)/(r3**3)
        x3=x3+vx3*dt
        vy3=vy3-(dt*y3*4*pi**2)/(r1**3)-(dt*y3*4*pi**2)/(r2**3)-(dt*y3*4*pi**2)/(r3**3)
        y3=y3+vy3*dt
	
#        y=y2-y1
 #       x=x2-x1
 #       ceta=math.atan2(y,x)
        t=t+dt
        print t

    #    a=a-a*0.0000001
figure2=plt.figure('b')
plot(x1_all,y1_all)
plot(x2_all,y2_all)
plot(x3_all,y3_all)
#figure1=plt.figure('a')
#fig2=plot(t_all,r_all)
#figure3=plt.figure('c')
#fig3=plot(t_all,ceta_all)
show()

