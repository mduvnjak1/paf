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
lista_akceleracija=[[a,t]]
lista_brzina=[[v,t]]
lista_x=[[x,t]]
for i in range(T/dt):
    t+=dt
    a+=da
    lista_akceleracija.apppend([a,t])
    v+=a*dt
    lista_brzina.append([v,t])
    x+=v*dt
    lista_x.append([x,t])



    
