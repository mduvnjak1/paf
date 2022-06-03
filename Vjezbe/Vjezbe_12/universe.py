from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
class Planet:
    def __init__(self):
        self.lista_vremena=[]
        self.v=np.array((0,0,0))
        self.xyz=np.array((0,0,0))
        self.a=np.array((0,0,0))
        self.lista_xyz=[]
        self.lista_v=[]
        self.lista_F=[]
        self.lista_a=[]
        self.x=[self.xyz[0]]
        self.y=[self.xyz[1]]
        self.z=[self.xyz[2]]
        self.m=1
    
    def set_initial_conditions(self, xyz, v, m):
        self.m=m
        self.v=v
        self.xyz=xyz
        self.lista_vremena.append(0)
        self.lista_xyz.append(self.xyz)
        self.lista_v.append(self.v)
    
    def reset(self):
        self.__init__()
    

def __interact(g1,g2,F,dt=10**4):
    g1.a=F(g1,g2)/g1.m
    g2.a=F(g2,g1)/g2.m
    g1.lista_vremena.append(g1.lista_vremena[-1]+dt)
    g2.lista_vremena.append(g2.lista_vremena[-1]+dt)
    g1.v=g1.v+g1.a*dt
    g2.v=g2.v+g2.a*dt
    g1.lista_v.append(g1.v)
    g2.lista_v.append(g2.v)
    g1.xyz=g1.xyz+g1.v*dt
    g2.xyz=g2.xyz+g2.v*dt
    g1.lista_xyz.append(g1.xyz)
    g2.lista_xyz.append(g2.xyz)
    g1.x=[self.xyz[0]]
    g2.y=[self.xyz[1]]
    self.z=[self.xyz[2]]
    self.x=[self.xyz[0]]
    self.y=[self.xyz[1]]
    self.z=[self.xyz[2]]
    
    
def __interact_rk(g1,g2,F,dt=10**4):
    g1k1v=(F(g1,g2)/g1.m)*dt
    g1k1=g1.v*dt
    g1k2v=(F(g1,g2)/g1.m)*dt
    g1k2=(g1.v+0.5*g1k1v)*dt
    g1k3v=(F(g1,g2)/g1.m)*dt
    g1k3=(g1.v+0.5*g1k2v)*dt
    g1k4v=(F(g1,g2)/g1.m)*dt
    g1k4=(g1.v+g1k3v)*dt
    g1.lista_vremena.append(g1.lista_vremena[-1]+dt)
    g1.v=g1.v+(g1k1v+2*g1k2v+2*g1k3v+g1k4v)/6
    g1.lista_v.append(g1.v)
    g1.xyz=g1.xyz+(g1k1+2*g1k2+2*g1k3+g1k4)/6
    g1.lista_xyz.append(g1.xyz)
    g1.a=F(g1,g2)/g1.m
    g1.lista_a.append(g1.a)

    g2k1v=(F(g2,g1)/g2.m)*dt
    g2k1=g2.v*dt
    g2k2v=(F(g2,g1)/g2.m)*dt
    g2k2=(g2.v+0.5*g2k1v)*dt
    g2k3v=(F(g2,g1)/g2.m)*dt
    g2k3=(g2.v+0.5*g2k2v)*dt
    g2k4v=(F(g2,g1)/g2.m)*dt
    g2k4=(g2.v+g2k3v)*dt
    g2.lista_vremena.append(g2.lista_vremena[-1]+dt)
    g2.v=g2.v+(g2k1v+2*g2k2v+2*g2k3v+g2k4v)/6
    g2.lista_v.append(g2.v)
    g2.xyz=g2.xyz+(g2k1+2*g2k2+2*g2k3+g2k4)/6
    g2.lista_xyz.append(g2.xyz)
    g2.a=F(g2,g1)/g2.m
    g2.lista_a.append(g2.a)
    
def plot_trajectory(lista_objekata,F,dt=10**4,T=31.557*10**6):
    g1x=[]
    g1y=[]
    g1z=[]
    g2x=[]
    g2y=[]
    g2z=[]    
    while (g1.lista_vremena[-1]<=T and g2.lista_vremena[-1]<=T):
        __interact(g1,g2,F,dt)
    for element in g1.lista_xyz:
        g1x.append(element[0])
        g1y.append(element[1])
        g1z.append(element[2])
    for element in g2.lista_xyz:
        g2x.append(element[0])
        g2y.append(element[1])
        g2z.append(element[2])
    plt.plot(g1x,g1y,label="Zemlja")
    plt.plot(g2x,g2y,label="Sunce")
    plt.legend(loc="upper left")

def plot_trajectory_rk(lista_objekata,F,dt=10**4,T=31.557*10**6):   
    while (lista_objekata[0].lista_vremena[-1]<=T):
        for g1 in lista_objekata:
            for g2 in lista_objekata:
                __interact(g1,g2,F,dt)
    for element in lista_objekata:
        plt.plot(element.x,element.y,label="Zemlja_rk")
    plt.legend(loc="upper left")