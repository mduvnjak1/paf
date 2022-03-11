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
lista_vremena=[t]
lista_akceleracija=[a]
lista_brzina=[v]
lista_položaja=[x]
for i in range(T/dt):
    t+=dt
    lista_vremena.append(t)
    a+=da
    lista_akceleracija.apppend(a)
    v+=a*dt
    lista_brzina.append(v)
    x+=v*dt
    lista_položaja.append(x)



    
