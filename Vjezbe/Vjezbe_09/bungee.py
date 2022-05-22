from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
class Projectile:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_akceleracija_y=[]
        self.lista_brzina_y=[]
        self.lista_polozaja_y=[]
        self.lista_energija_kin=[]
        self.lista_energija_pot=[]
        self.lista_energija_elastic=[]
        self.lista_energija_total=[]
        self.p=0
        self.Cd=0
        self.A=0
        self.m=1
        self.k=0
        self.l=0
        self.F=0
    
    def set_initial_conditions(self, vy, y, Cd, p, A, m, k, l, F):
        self.y=y
        self.p=p
        self.Cd=Cd
        self.A=A
        self.m=m
        self.k=k
        self.l=l
        self.F=F
        self.lista_vremena.append(0)
        self.lista_brzina_y.append(vy)
        self.lista_polozaja_y.append(y)
        self.lista_akceleracija_y.append(F(self.p, self.Cd, self.A, self.k, self.y, self.l, self.lista_brzina_y[-1], self.lista_polozaja_y[-1])/self.m-9.81)
        self.lista_energija_kin.append(0.5*self.m*self.lista_brzina_y[-1]**2)
        self.lista_energija_pot.append(self.m*9.81*self.lista_polozaja_y[-1])
        if np.abs(self.lista_polozaja_y[-1]-self.y)>self.l:
            self.lista_energija_elastic.append(0.5*self.k*(self.lista_polozaja_y[-1]-self.l)**2)
        else:
            self.lista_energija_elastic.append(0)
        self.lista_energija_total.append(self.lista_energija_kin[-1]+self.lista_energija_pot[-1]+self.lista_energija_elastic[-1])

    def reset(self):
        self.__init__()
    
    def __move(self,dt=0.1):
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+self.lista_akceleracija_y[-1]*dt)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+self.lista_brzina_y[-1]*dt)
        self.lista_akceleracija_y.append(self.F(self.p, self.Cd, self.A, self.k, self.y, self.l, self.lista_brzina_y[-1], self.lista_polozaja_y[-1])/self.m-9.81)
        self.lista_energija_kin.append(0.5*self.m*self.lista_brzina_y[-1]**2)
        self.lista_energija_pot.append(self.m*9.81*self.lista_polozaja_y[-1])
        if np.abs(self.lista_polozaja_y[-1]-self.y)>self.l:
            self.lista_energija_elastic.append(0.5*self.k*(self.lista_polozaja_y[-1]-self.y+self.l)**2)
        else:
            self.lista_energija_elastic.append(0)
        self.lista_energija_total.append(self.lista_energija_kin[-1]+self.lista_energija_pot[-1]+self.lista_energija_elastic[-1])
    
    def __move_rk(self,dt=0.1):
        k1vy=(self.F(self.p, self.Cd, self.A, self.k, self.y, self.l, self.lista_brzina_y[-1], self.lista_polozaja_y[-1])/self.m-9.81)*dt
        k1y=self.lista_brzina_y[-1]*dt
        k2vy=(self.F(self.p, self.Cd, self.A, self.k, self.y, self.l, (self.lista_brzina_y[-1]+0.5*k1vy), self.lista_polozaja_y[-1])/self.m-9.81)*dt
        k2y=(self.lista_brzina_y[-1]+0.5*k1vy)*dt
        k3vy=(self.F(self.p, self.Cd, self.A, self.k, self.y, self.l, (self.lista_brzina_y[-1]+0.5*k2vy), self.lista_polozaja_y[-1])/self.m-9.81)*dt
        k3y=(self.lista_brzina_y[-1]+0.5*k2vy)*dt
        k4vy=(self.F(self.p, self.Cd, self.A, self.k, self.y, self.l, (self.lista_brzina_y[-1]+k3vy), self.lista_polozaja_y[-1])/self.m-9.81)*dt
        k4y=(self.lista_brzina_y[-1]+k3vy)*dt
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+(k1vy+2*k2vy+2*k3vy+k4vy)/6)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+(k1y+2*k2y+2*k3y+k4y)/6)
        self.lista_energija_kin.append(0.5*self.m*self.lista_brzina_y[-1]**2)
        self.lista_energija_pot.append(self.m*9.81*self.lista_polozaja_y[-1])
        if np.abs(self.lista_polozaja_y[-1]-self.y)>self.l:
            self.lista_energija_elastic.append(0.5*self.k*(self.lista_polozaja_y[-1]-self.y+self.l)**2)
        else:
            self.lista_energija_elastic.append(0)
        self.lista_energija_total.append(self.lista_energija_kin[-1]+self.lista_energija_pot[-1]+self.lista_energija_elastic[-1])
    
    def plot_y_t(self,T,dt=0.01):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_polozaja_y,label="Euler")
        plt.legend(loc="upper left")
    
    def plot_y_t_rk(self,T,dt=0.01):
        while self.lista_vremena[-1]<=T:
            self.__move_rk(dt)
        plt.plot(self.lista_vremena,self.lista_polozaja_y,label="Runge kutta")
        plt.legend(loc="upper left")

    def plot_energija_t(self,T,dt=0.01):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_energija_kin,label="E.kin")
        plt.plot(self.lista_vremena,self.lista_energija_pot,label="E.pot")
        plt.plot(self.lista_vremena,self.lista_energija_elastic,label="E.el")
        plt.plot(self.lista_vremena,self.lista_energija_total,label="E.total")
        plt.legend(loc="upper left")
    
    
    def plot_energija_t_rk(self,T,dt=0.01):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_energija_kin,label="E.kin")
        plt.plot(self.lista_vremena,self.lista_energija_pot,label="E.pot")
        plt.plot(self.lista_vremena,self.lista_energija_elastic,label="E.el")
        plt.plot(self.lista_vremena,self.lista_energija_total,label="E.total")
        plt.legend(loc="upper left")