from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
class Projectile:
    def __init__(self):
        self.lista_vremena=[0]
        self.v=np.array((0,0,0))
        self.xyz=np.array((0,0,0))
        self.E=0
        self.B=0
        self.Ev=0
        self.Bv=0
        self.a=0
        self.lista_xyz=[]
        self.lista_v=[]
        self.lista_E=[]
        self.lista_B=[]
        self.lista_a=[]
        self.m=1
        self.q=1
        self.F=0
        self.T=1
    
    def set_initial_conditions(self, xyz, v, E, B, m, q, F,T=10):
        self.m=m
        self.q=q
        self.F=F
        self.v=v
        self.xyz=xyz
        self.E=E
        self.B=B
        self.T=T
        self.Ev=E(self.lista_vremena[-1],self.T)
        self.Bv=B(self.lista_vremena[-1],self.T)
        self.a=F(self.q, self.Ev, self.v, self.Bv)/m
        self.lista_xyz.append(self.xyz)
        self.lista_v.append(self.v)
        self.lista_a.append(self.a)
    
    def reset(self):
        self.__init__()
    
    def __move(self,dt=0.1):
        self.Ev=self.E(self.lista_vremena[-1],self.T)
        self.Bv=self.B(self.lista_vremena[-1],self.T)
        self.v=self.v+self.a*dt
        self.lista_v.append(self.v)
        self.xyz=self.xyz+self.v*dt
        self.lista_xyz.append(self.xyz)
        self.a=self.F(self.q, self.Ev, self.v, self.Bv)/self.m
        self.lista_a.append(self.a)
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
    
    def __move_rk(self,dt=0.1):
        self.Ev=self.E(self.lista_vremena[-1],self.T)
        self.Bv=self.B(self.lista_vremena[-1],self.T)
        k1v=(self.F(self.q, self.Ev, self.v, self.Bv)/self.m)*dt
        k1=self.v*dt
        k2v=(self.F(self.q, self.Ev, (self.v+0.5*k1v), self.Bv)/self.m)*dt
        k2=(self.v+0.5*k1v)*dt
        k3v=(self.F(self.q, self.Ev, (self.v+0.5*k2v), self.Bv)/self.m)*dt
        k3=(self.v+0.5*k2v)*dt
        k4v=(self.F(self.q, self.Ev, (self.v+0.5*k3v), self.Bv)/self.m)*dt
        k4=(self.v+k3v)*dt
        self.v=self.v+(k1v+2*k2v+2*k3v+k4v)/6
        self.lista_v.append(self.v)
        self.xyz=self.xyz+(k1+2*k2+2*k3+k4)/6
        self.lista_xyz.append(self.xyz)
        self.a=self.F(self.q, self.Ev, self.v, self.Bv)/self.m
        self.lista_a.append(self.a)
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
    
    def plot_trajectory(self,dt=0.01, T=50):
        x=[]
        y=[]
        z=[]
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        for element in self.lista_xyz:
            x.append(element[0])
            y.append(element[1])
            z.append(element[2])
        fig = plt.figure(figsize = (8,8))
        ax = plt.axes(projection='3d')
        ax.grid()
        ax.plot3D(x,y,z,label="Euler")
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