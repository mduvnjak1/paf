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
        self.v=(self.v[0]+self.a[0]*dt, self.v[1]+self.a[1]*dt, self.v[2]+self.a[2]*dt)
        self.lista_v.append(self.v)
        self.xyz=(self.xyz[0]+self.v[0]*dt, self.xyz[1]+self.v[1]*dt, self.xyz[2]+self.v[2]*dt)
        self.lista_xyz.append(self.xyz)
        self.a=self.F(self.q, self.E, self.v, self.B)/self.m
        self.lista_a.append(self.a)
    
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
        ax.plot3D(x,y,z)
    def plot_trajectory_rk(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move_rk(dt)
        plt.plot(self.lista_polozaja_x,self.lista_polozaja_y,label="Runge kutta")
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
            lista_dometa.append(self.range_rk(dt))
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
            lista_dometa.append(self.range_rk(dt))
            m+=dm
        plt.plot(lista_m,lista_dometa)
        plt.show()