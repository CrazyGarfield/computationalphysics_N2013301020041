import matplotlib.pylab as plt

N_Aall=[]
N_Ball=[]
t=[]
N_Aall.append(100.0)
N_Ball.append(0.0)
t.append(0.0)
T=1
dt=0.01
endtime=5.0
for i in range(int(endtime/dt)):
    equ1=N_Aall[-1]+(N_Ball[-1]-N_Aall[-1])/T*dt
    equ2=N_Ball[-1]+(N_Aall[-1]-N_Ball[-1])/T*dt
    N_Aall.append(equ1);N_Ball.append(equ2)
    t.append(dt*(i+1))



line1,=plt.plot(t,N_Aall,'r--')
line2,=plt.plot(t,N_Ball,'b--')
plt.xlabel('Time/(s)')
plt.ylabel('Nuclei Number')
plt.legend((line1,line2),('Number of Nuclei A','Number of Nuclei B'))
plt.title('The Time')
