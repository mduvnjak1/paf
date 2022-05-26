from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
class Planet:
    def __init__(self):
        self.lista_vremena=[]
        self.v=np.array((0,0,0))
        self.xyz=np.array((0,0,0))
        self.F=np.array((0,0,0))
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
    
    def reset(self):
        self.__init__()
    

def __interact(g1,g2,F,dt=0.1):
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
    
def __move_rk(self,dt=0.1):
    k1v=(self.F(self.q, self.E, self.v, self.B)/self.m)*dt
    k1=self.v*dt
    k2v=(self.F(self.q, self.E, (self.v+0.5*k1v), self.B)/self.m)*dt
    k2=(self.v+0.5*k1v)*dt
    k3v=(self.F(self.q, self.E, (self.v+0.5*k2v), self.B)/self.m)*dt
    k3=(self.v+0.5*k2v)*dt
    k4v=(self.F(self.q, self.E, (self.v+0.5*k3v), self.B)/self.m)*dt
    k4=(self.v+k3v)*dt
    self.lista_vremena.append(self.lista_vremena[-1]+dt)
    self.v=self.v+(k1v+2*k2v+2*k3v+k4v)/6
    self.lista_v.append(self.v)
    self.xyz=self.xyz+(k1+2*k2+2*k3+k4)/6
    self.lista_xyz.append(self.xyz)
    self.a=self.F(self.q, self.E, self.v, self.B)/self.m
    self.lista_a.append(self.a)
    
def plot_trajectory(g1,g2,F,dt=10**4, T=150*10**6):
    while g1.lista_vremena[-1]<=T:
        __interact(g1,g2,F,dt=0.1)
    for element in g1.lista_xyz:
        g1.x.append(element[0])
        g1.y.append(element[1])
        g1.z.append(element[2])
    for element in g2.lista_xyz:
        g2.x.append(element[0])
        g2.y.append(element[1])
        g2.z.append(element[2])
    fig = plt.figure(figsize = (8,8))
    ax = plt.axes(projection='3d')
    ax.grid()
    ax.plot3D(g1.x,g1.y,g1.z,label="Euler")
    ax.plot3D(g2.x,g2.y,g2.z,label="Euler")
    ax.legend(loc="upper left")
def plot_trajectory_rk(self,dt=0.01, T=50):
    x=[]
    y=[]
    z=[]
    while self.lista_vremena[-1]<=T:
        self.__move_rk(dt)
    for element in self.lista_xyz:
        x.append(element[0])
        y.append(element[1])
        z.append(element[2])
    fig = plt.figure(figsize = (8,8))
    ax = plt.axes(projection='3d')
    ax.grid()
    ax.plot3D(x,y,z,label="Runge kutta")
    ax.legend(loc="upper left")