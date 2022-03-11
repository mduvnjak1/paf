import numpy as np
import matplotlib as plt
F=float(input('Unesite iznos sile u [N]: '))
m=float(input('Unesite izmos mase u [kg]: '))
a=F/m
da=0
v=0
x=0
t=0
dt=0.1
T=10
for i in range(T/dt+1):
    t+=dt
    a+=da
    plt.plot(a,t)
plt.savefig('a,t graf')
for i in range(T/dt+1):
    t+=dt
    a+=da
    v+=a*dt
    plt.plot(v,t)
plt.savefig('v,t graf')
for i in range(T/dt+1):
    t+=dt
    a+=da
    v+=a*dt
    x+=v*dt
    plt.plot(x,t)
plt.savefig('x,t graf')