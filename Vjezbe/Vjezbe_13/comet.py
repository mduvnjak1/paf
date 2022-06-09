from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
class Planet:
    def __init__(self,name):
        self.name=name
        self.lista_vremena=[]
        self.v=np.array((0,0,0))
        self.xyz=np.array((0,0,0))
        self.a=np.array((0,0,0))
        self.lista_xyz=[]
        self.lista_v=[]
        self.lista_F=[]
        self.lista_a=[]
        self.x=[]
        self.y=[]
        self.z=[]
        self.m=1
        self.r=1
    
    def set_initial_conditions(self, xyz, v, m, r):
        self.m=m
        self.r=r
        self.v=v
        self.xyz=xyz
        self.lista_vremena.append(0)
        self.lista_xyz.append(self.xyz)
        self.lista_v.append(self.v)
        self.x=[self.xyz[0]]
        self.y=[self.xyz[1]]
        self.z=[self.xyz[2]]
    

def __interact(lista_objekata,F,dt=10**5):
    for g1 in lista_objekata:
        g1.a=np.array((0,0,0))
        for g2 in lista_objekata:
            if (g1!=g2) and (np.linalg.norm(g2.xyz-g1.xyz)<=(g1.r+g2.r)):
                new=Planet(g1.name+g2.name)
                new.set_initial_conditions((g1.xyz*g1.m+g2.xyz*g2.m)/g1.m+g2.m, (g1.v*g1.m+g2.v*g2.m)/g1.m+g2.m, g1.m+g2.m, (g1.r*g1.m+g2.r*g2.m)/g1.m+g2.m)
                lista_objekata.append(new)
                g1.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1,0)
                g2.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1,0)
            if g1!=g2:
                g1.a=g1.a+F(g1,g2)/g1.m
        g1.lista_vremena.append(g1.lista_vremena[-1]+dt)
        g1.v=g1.v+g1.a*dt
        g1.lista_v.append(g1.v)
        g1.xyz=g1.xyz+g1.v*dt
        g1.lista_xyz.append(g1.xyz)
        g1.x.append(g1.xyz[0])
        g1.y.append(g1.xyz[1])
        g1.z.append(g1.xyz[2])

def universe_plot_trajectory(lista_objekata,F,dt=10**5,T=5*31.557*10**6):   
    while (lista_objekata[0].lista_vremena[-1]<=T):
        __interact(lista_objekata,F,dt)
    for element in lista_objekata:
        plt.plot(element.x,element.y,label=str(element.name))
    plt.legend(loc="upper left")

def universe_animate_trajectory(lista_objekata,F,dt=5*10**5,T=5*31.557*10**6):   
    while (lista_objekata[0].lista_vremena[-1]<=T):
        __interact(lista_objekata,F,dt)
        plt.xlim(-3.5*10**11,3.5*10**11)
        plt.ylim(-3.5*10**11,3.5*10**11)
        for element in lista_objekata:
            plt.scatter(element.xyz[0],element.xyz[1],label=str(element.name))
            plt.plot(element.x,element.y)
            plt.legend(loc="upper left")
        plt.pause(0.00001)
        plt.clf()