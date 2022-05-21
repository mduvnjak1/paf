from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
class Projectile:
    def __init__(self):
        self.lista_vremena=[]
        self.v=np.array((0,0,0))
        self.xyz=np.array((0,0,0))
        self.E=np.array((0,0,0))
        self.B=np.array((0,0,0))
        self.a=np.array((0,0,0))
        self.lista_xyz=[]
        self.lista_v=[]
        self.lista_E=[]
        self.lista_B=[]
        self.lista_a=[]
        self.m=1
        self.q=1
        self.F=0
    
    def set_initial_conditions(self, xyz, v, E, B, m, q, F):
        self.m=m
        self.q=q
        self.F=F
        self.v=v
        self.xyz=xyz
        self.E=E
        self.B=B
        self.a=F(self.q, self.E, self.v, self.B)/m
        self.lista_vremena.append(0)
        self.lista_xyz.append(self.xyz)
        self.lista_v.append(self.v)
        self.lista_a.append(self.a)
    
    def reset(self):
        self.__init__()
    
    def __move(self,dt=0.1):
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.v=self.v+self.a*dt
        self.lista_v.append(self.v)
        self.xyz=self.xyz+self.v*dt
        self.lista_xyz.append(self.xyz)
        self.a=self.F(self.q, self.E, self.v, self.B)/self.m
        self.lista_a.append(self.a)
    
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