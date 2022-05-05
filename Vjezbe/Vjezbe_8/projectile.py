from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
class Projectile:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_akceleracija_x=[]
        self.lista_akceleracija_y=[]
        self.lista_brzina_x=[]
        self.lista_brzina_y=[]
        self.lista_brzina=[]
        self.lista_polozaja_x=[]
        self.lista_polozaja_y=[]
        self.p=0
        self.Cd=0
        self.A=0
        self.m=1
        self.F=0
    
    def set_initial_conditions(self, v, angle, x, y, Cd, p, A, m, F):
        self.p=p
        self.Cd=Cd
        self.A=A
        self.m=m
        self.F=F
        vx=v*np.cos(angle)
        vy=v*np.sin(angle)
        self.lista_vremena.append(0)
        self.lista_brzina_x.append(vx)
        self.lista_brzina_y.append(vy)
        self.lista_brzina.append(v)
        self.lista_polozaja_x.append(x)
        self.lista_polozaja_y.append(y)
        self.lista_akceleracija_x.append(F(self.p, self.Cd, self.A, self.lista_brzina[-1])*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))
        self.lista_akceleracija_y.append(F(self.p, self.Cd, self.A, self.lista_brzina[-1])*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)
    
    def reset(self):
        self.__init__()
    
    def __move(self,dt=0.1):
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina_x.append(self.lista_brzina_x[-1]+self.lista_akceleracija_x[-1]*dt)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+self.lista_akceleracija_y[-1]*dt)
        self.lista_brzina.append(np.sqrt(self.lista_brzina_x[-1]**2+self.lista_brzina_y[-1]**2))
        self.lista_polozaja_x.append(self.lista_polozaja_x[-1]+self.lista_brzina_x[-1]*dt)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+self.lista_brzina_y[-1]*dt)
        self.lista_akceleracija_x.append(self.F(self.p, self.Cd, self.A, self.lista_brzina[-1])*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))
        self.lista_akceleracija_y.append(self.F(self.p, self.Cd, self.A, self.lista_brzina[-1])*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)
    
    def __move_rk(self,dt=0.1):
        k1vx=(self.F(self.p, self.Cd, self.A, self.lista_brzina[-1])*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k1vy=(self.F(self.p, self.Cd, self.A, self.lista_brzina[-1])*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k1x=self.lista_brzina_x[-1]*dt
        k1y=self.lista_brzina_y[-1]*dt
        k2vx=(self.F(self.p, self.Cd, self.A, (self.lista_brzina[-1]+0.5*k1vx))*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k2vy=(self.F(self.p, self.Cd, self.A, (self.lista_brzina[-1]+0.5*k1vy))*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k2x=(self.lista_brzina_x[-1]+0.5*k1vx)*dt
        k2y=(self.lista_brzina_y[-1]+0.5*k1vy)*dt
        k3vx=(self.F(self.p, self.Cd, self.A, (self.lista_brzina[-1]+0.5*k2vx))*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k3vy=(self.F(self.p, self.Cd, self.A, (self.lista_brzina[-1]+0.5*k2vy))*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k3x=(self.lista_brzina_x[-1]+0.5*k2vx)*dt
        k3y=(self.lista_brzina_y[-1]+0.5*k2vy)*dt
        k4vx=(self.F(self.p, self.Cd, self.A, (self.lista_brzina[-1]+k3vx))*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k4vy=(self.F(self.p, self.Cd, self.A, (self.lista_brzina[-1]+k3vy))*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k4x=(self.lista_brzina_x[-1]+k3vx)*dt
        k4y=(self.lista_brzina_y[-1]+k3vy)*dt
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina_x.append(self.lista_brzina_x[-1]+(k1vx+2*k2vx+2*k3vx+k4vx)/6)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+(k1vy+2*k2vy+2*k3vy+k4vy)/6)
        self.lista_brzina.append(np.sqrt(self.lista_brzina_x[-1]**2+self.lista_brzina_y[-1]**2))
        self.lista_polozaja_x.append(self.lista_polozaja_x[-1]+(k1x+2*k2x+2*k3x+k4x)/6)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+(k1y+2*k2y+2*k3y+k4y)/6)
    
    def plot_trajectory(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        plt.plot(self.lista_polozaja_x,self.lista_polozaja_y,label="Euler")
        plt.legend(loc="upper left")
    def plot_trajectory_rk(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move_rk(dt)
        plt.plot(self.lista_polozaja_x,self.lista_polozaja_y,label="Runge kutta")
        plt.legend(loc="upper left")
    def range(self,dt=0.1):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        return (self.lista_polozaja_x[-1])
    def domet_analiticki(self):
        g=self.lista_akceleracija_y[0]
        vx=self.lista_brzina_x[0]
        vy=self.lista_brzina_y[0]
        x=self.lista_polozaja_x[0]
        y=self.lista_polozaja_y[0]
        D=x+vx*((-vy-np.sqrt(vy**2+2*g*y))/g)
        return D
    def error(self,dt=0.1):
        return(np.abs(self.domet_analiticki()-self.range(dt))/self.domet_analiticki())
    def error_dt_graf(self,v,angle,x,y,ddt=0.05,N=50):
        lista_dt=[]
        lista_error=[]
        dt=0
        for i in range(N):
            dt+=ddt
            lista_dt.append(dt)
            lista_error.append(self.error(dt))
            self.reset()
            self.set_initial_conditions(v,angle,x,y)
        plt.plot(lista_dt,lista_error)
        plt.show()
    def graf_domet_kut(self,x,y,v,dangle=0.1,dt=0.01):
        angle=0
        lista_kuteva=[]
        lista_dometa=[]
        while angle<=1.57:
            self.reset()
            self.set_initial_conditions(v,angle,x,y)
            lista_kuteva.append(angle)
            lista_dometa.append(self.range(dt))
            angle+=dangle
        plt.plot(lista_kuteva,lista_dometa)
        plt.show()
    def graf_ukupno_vrijeme_kut(self,x,y,v,dangle=0.1,dt=0.01):
        angle=0
        lista_kuteva=[]
        lista_ukupnog_vremena=[]
        while angle<=1.57:
            self.reset()
            self.set_initial_conditions(v,angle,x,y)
            lista_kuteva.append(angle)
            lista_ukupnog_vremena.append(self.total_time(dt))
            angle+=dangle
        plt.plot(lista_kuteva,lista_ukupnog_vremena)
        plt.show()