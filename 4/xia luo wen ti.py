import matplotlib.pyplot as plt
import numpy as np
#analytical line
x=np.linspace(0.0,20.0,201)
def f(x): 
    return (1-np.exp(-x))*10
#numerical line
v_all=[]
t_all=[]
v=0
t=0
a=10;b=1
dt=0.05

endtime=20
while t < endtime:
    
    v=v+dt*(a-b*v)
    t=t+dt

    v_all.append(v)
    t_all.append(t)
  
line1,=plt.plot(t_all,v_all,'ro')
line2,=plt.plot(x,f(x),'b--')
plt.xlabel("time/(s)")
plt.ylabel("velocity/(m/s)")
plt.legend((line1,line2),('numerical line','analytical line'))
plt.title("A Ball Falling with Friction")
plt.show()

