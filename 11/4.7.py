import numpy
import math
import pickle
from pylab import *

x1=1
y1=1
x2=-1
y2=-1
vx1=0
vx2=0
vy1=2
vy2=-2
pi=3.1415926
t=0
dt=0.002
r=0
#vy1=float(raw_input())
#vy2=float(raw_input())
#vx1=float(raw_input())
a=1

x1_all=[]
y1_all=[]
x2_all=[]
y2_all=[]
r_all=[]
t_all=[]

while(t<23):
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
	a=a-0.00001*a


figure2=plt.figure('b')
plot(x1_all,y1_all)
plot(x2_all,y2_all)
savefig('fig4.jpg')
title('the orbit of double stars')
xlabel('x axis')
ylabel('y axis')
legend(('star 1','star 2'),'best')


figure1=plt.figure('a')
plot(r_all,t_all)
title('the space between double stars')
xlabel('time')
ylabel('distance between two stars')
legend(('period',),'best')
savefig('fig3.jpg')
show()

