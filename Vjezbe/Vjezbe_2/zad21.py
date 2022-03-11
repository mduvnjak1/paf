import numpy as np
import matplotlib.pyplot as plt
F=10
m=5
a=F/m
da=0
v=0
x=0
t=0
dt=0.1
T=10
n=round(T/dt)
lista_vremena=[t]
lista_akceleracija=[a]
lista_brzina=[v]
lista_položaja=[x]
for i in range(n):
    t+=dt
    lista_vremena.append(t)
    a+=da
    lista_akceleracija.append(a)
    v+=a*dt
    lista_brzina.append(v)
    x+=v*dt
    lista_položaja.append(x)
plt.plot(lista_vremena,lista_akceleracija)
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [m/s^2]')
plt.show()
plt.plot(lista_vremena,lista_brzina)
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.show()
plt.plot(lista_vremena,lista_položaja)
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')
plt.show()
