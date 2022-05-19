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
        self.lista_povrsina=[]
        self.lista_polozaja_x=[]
        self.lista_polozaja_y=[]
        self.p=0
        self.Cd=0
        self.r=0
        self.oblik='sfera'
        self.m=1
        self.F=0
    
    def set_initial_conditions(self, v, angle, x, y, Cd, p, m, F, oblik, r):
        self.p=p
        self.Cd=Cd
        self.r=r
        self.oblik=oblik
        self.m=m
        self.F=F
        vx=v*np.cos(angle)
        vy=v*np.sin(angle)
        self.lista_povrsina=[]
        self.lista_vremena.append(0)
        self.lista_brzina_x.append(vx)
        self.lista_brzina_y.append(vy)
        self.lista_brzina.append(v)
        if oblik=='sfera':
            self.lista_povrsina.append(self.r**2*np.pi)
        elif oblik=='kocka':
            self.lista_povrsina.append((np.abs(vx)+np.abs(vy))*4*self.r**2/self.lista_brzina[-1])
        self.lista_polozaja_x.append(x)
        self.lista_polozaja_y.append(y)
        self.lista_akceleracija_x.append(F(self.p, self.Cd, self.lista_povrsina[-1], self.lista_brzina[-1])*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))
        self.lista_akceleracija_y.append(F(self.p, self.Cd, self.lista_povrsina[-1], self.lista_brzina[-1])*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)
    
    def reset(self):
        self.__init__()
    
    def __move(self,dt=0.1):
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina_x.append(self.lista_brzina_x[-1]+self.lista_akceleracija_x[-1]*dt)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+self.lista_akceleracija_y[-1]*dt)
        self.lista_brzina.append(np.sqrt(self.lista_brzina_x[-1]**2+self.lista_brzina_y[-1]**2))
        if self.oblik=='sfera':
            self.lista_povrsina.append(self.r**2*np.pi)
        elif self.oblik=='kocka':
            self.lista_povrsina.append((np.abs(self.lista_brzina_x[-1])+np.abs(self.lista_brzina_y[-1]))*4*self.r**2/self.lista_brzina[-1])
        self.lista_polozaja_x.append(self.lista_polozaja_x[-1]+self.lista_brzina_x[-1]*dt)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+self.lista_brzina_y[-1]*dt)
        self.lista_akceleracija_x.append(self.F(self.p, self.Cd, self.lista_povrsina[-1], self.lista_brzina[-1])*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))
        self.lista_akceleracija_y.append(self.F(self.p, self.Cd, self.lista_povrsina[-1], self.lista_brzina[-1])*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)
    
    def __move_rk(self,dt=0.1):
        k1vx=(self.F(self.p, self.Cd, self.lista_povrsina[-1], self.lista_brzina[-1])*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k1vy=(self.F(self.p, self.Cd, self.lista_povrsina[-1], self.lista_brzina[-1])*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k1x=self.lista_brzina_x[-1]*dt
        k1y=self.lista_brzina_y[-1]*dt
        k2vx=(self.F(self.p, self.Cd, self.lista_povrsina[-1], (self.lista_brzina[-1]+0.5*k1vx))*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k2vy=(self.F(self.p, self.Cd, self.lista_povrsina[-1], (self.lista_brzina[-1]+0.5*k1vy))*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k2x=(self.lista_brzina_x[-1]+0.5*k1vx)*dt
        k2y=(self.lista_brzina_y[-1]+0.5*k1vy)*dt
        k3vx=(self.F(self.p, self.Cd, self.lista_povrsina[-1], (self.lista_brzina[-1]+0.5*k2vx))*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k3vy=(self.F(self.p, self.Cd, self.lista_povrsina[-1], (self.lista_brzina[-1]+0.5*k2vy))*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k3x=(self.lista_brzina_x[-1]+0.5*k2vx)*dt
        k3y=(self.lista_brzina_y[-1]+0.5*k2vy)*dt
        k4vx=(self.F(self.p, self.Cd, self.lista_povrsina[-1], (self.lista_brzina[-1]+k3vx))*self.lista_brzina_x[-1]/(self.m*self.lista_brzina[-1]))*dt
        k4vy=(self.F(self.p, self.Cd, self.lista_povrsina[-1], (self.lista_brzina[-1]+k3vy))*self.lista_brzina_y[-1]/(self.m*self.lista_brzina[-1])-9.81)*dt
        k4x=(self.lista_brzina_x[-1]+k3vx)*dt
        k4y=(self.lista_brzina_y[-1]+k3vy)*dt
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina_x.append(self.lista_brzina_x[-1]+(k1vx+2*k2vx+2*k3vx+k4vx)/6)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+(k1vy+2*k2vy+2*k3vy+k4vy)/6)
        self.lista_brzina.append(np.sqrt(self.lista_brzina_x[-1]**2+self.lista_brzina_y[-1]**2))
        if self.oblik=='sfera':
            self.lista_povrsina.append(self.r**2*np.pi)
        elif self.oblik=='kocka':
            self.lista_povrsina.append((np.abs(self.lista_brzina_x[-1])+np.abs(self.lista_brzina_y[-1]))*4*self.r**2/self.lista_brzina[-1])
        self.lista_polozaja_x.append(self.lista_polozaja_x[-1]+(k1x+2*k2x+2*k3x+k4x)/6)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+(k1y+2*k2y+2*k3y+k4y)/6)
    
    def plot_trajectory(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        plt.plot(self.lista_polozaja_x,self.lista_polozaja_y,label=self.oblik)
        plt.legend(loc="upper left")
    def plot_trajectory_rk(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move_rk(dt)
        plt.plot(self.lista_polozaja_x,self.lista_polozaja_y,label=self.oblik)
        plt.legend(loc="upper left")
    def range(self,dt=0.1):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        return (self.lista_polozaja_x[-1])
    def range_rk(self,dt=0.1):
        while self.lista_polozaja_y[-1]>=0:
            self.__move_rk(dt)
        return (self.lista_polozaja_x[-1])
    def graf_domet_Cd(self, v, angle, x, y, p, A, m, F, dCd, dt=0.01):
        Cd=0
        lista_Cd=[]
        lista_dometa=[]
        while Cd<=1:
            self.reset()
            self.set_initial_conditions( v, angle, x, y, Cd, p, A, m, F)
            lista_Cd.append(Cd)
            lista_dometa.append(self.range(dt))
            Cd+=dCd
        plt.plot(lista_Cd,lista_dometa)
        plt.show()
    def graf_domet_masa(self, v, angle, x, y, p, A, Cd, F, m_min, m_maks, dm, dt=0.01):
        m=m_min
        lista_m=[]
        lista_dometa=[]
        while m<=m_maks:
            self.reset()
            self.set_initial_conditions( v, angle, x, y, Cd, p, A, m, F)
            lista_m.append(m)
            lista_dometa.append(self.range(dt))
            m+=dm
        plt.plot(lista_m,lista_dometa)
        plt.show()