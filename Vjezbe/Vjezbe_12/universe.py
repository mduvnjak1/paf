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
    
    def set_initial_conditions(self, xyz, v, m):
        self.m=m
        self.v=v
        self.xyz=xyz
        self.lista_vremena.append(0)
        self.lista_xyz.append(self.xyz)
        self.lista_v.append(self.v)
        self.x=[self.xyz[0]]
        self.y=[self.xyz[1]]
        self.z=[self.xyz[2]]
    
    def reset(self):
        self.__init__()
    

def __interact(lista_objekata,F,dt=10**5):
    for g1 in lista_objekata:
        g1.a=np.array((0,0,0))
        for g2 in lista_objekata:
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
        plt.xlim(-2.5*10**11,2.5*10**11)
        plt.ylim(-2.5*10**11,2.5*10**11)
        for element in lista_objekata:
            plt.scatter(element.xyz[0],element.xyz[1],label=str(element.name))
            plt.plot(element.x,element.y)
            plt.legend(loc="upper left")
        plt.pause(0.0001)
        plt.clf()