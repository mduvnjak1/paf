import numpy as np
import matplotlib.pyplot as plt
v=100
alpha=np.pi/3
vx=v*np.cos(alpha)
vy=v*np.sin(alpha)
t=0
dt=0.1
T=10
n=round(T/dt)
ax=0
dax=0
ay=-10
day=0
x=0
y=0
lista_vremena=[t]
lista_akceleracija_x=[ax]
lista_akceleracija_y=[ay]
lista_brzina_x=[vx]
lista_brzina_y=[vy]
lista_položaja_x=[x]
lista_položaja_y=[y]
for i in range(n):
    t+=dt
    lista_vremena.append(t)
    ax+=dax
    lista_akceleracija_x.append(ax)
    ay+=day
    lista_akceleracija_y.append(ay)
    vx+=ax*dt
    lista_brzina_x.append(vx)
    vy+=ay*dt
    lista_brzina_y.append(vy)
    x+=vx*dt
    lista_položaja_x.append(x)
    y+=vy*dt
    lista_položaja_y.append(y)
plt.plot(lista_vremena,lista_akceleracija_x)
plt.xlabel('Time [s]')
plt.ylabel('Acceleration x [m/s^2]')
plt.show()
plt.plot(lista_vremena,lista_akceleracija_y)
plt.xlabel('Time [s]')
plt.ylabel('Acceleration y [m/s^2]')
plt.show()
plt.plot(lista_vremena,lista_brzina_x)
plt.xlabel('Time [s]')
plt.ylabel('Velocity x [m/s]')
plt.show()
plt.plot(lista_vremena,lista_brzina_y)
plt.xlabel('Time [s]')
plt.ylabel('Velocity y [m/s]')
plt.show()
plt.plot(lista_vremena,lista_položaja_x)
plt.xlabel('Time [s]')
plt.ylabel('Position x [m]')
plt.show()
plt.plot(lista_vremena,lista_položaja_y)
plt.xlabel('Time [s]')
plt.ylabel('Position y [m]')
plt.show()