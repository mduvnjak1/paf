import numpy as np
import matplotlib.pyplot as plt
class ProjectileDrop:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_akceleracija_x=[]
        self.lista_akceleracija_y=[]
        self.lista_brzina_x=[]
        self.lista_brzina_y=[]
        self.lista_brzina=[]
        self.lista_polozaja_x=[]
        self.lista_polozaja_y=[]
        print('Objekt je stvoren')
    def set_initial_conditions_potvrda(self, vx, x, y, t=0):
        self.lista_vremena=[t]
        self.lista_akceleracija_x=[0]
        self.lista_akceleracija_y=[-9.81]
        self.lista_brzina_x=[vx]
        self.lista_brzina_y=[0]
        self.lista_brzina=[vx]
        self.lista_polozaja_x=[x]
        self.lista_polozaja_y=[y]
        print('Postavljena brzina je',vx,'a postavljena visina je',y)
    def set_initial_conditions(self, vx, x, y, t=0):
        self.lista_vremena=[t]
        self.lista_akceleracija_x=[0]
        self.lista_akceleracija_y=[-9.81]
        self.lista_brzina_x=[vx]
        self.lista_brzina_y=[0]
        self.lista_brzina=[vx]
        self.lista_polozaja_x=[x]
        self.lista_polozaja_y=[y]
    def reset(self):
        self.__init__()
    def promjena_visine(self,h):
        self.set_initial_conditions(self.lista_brzina_x[0],self.lista_polozaja_x[0],h)
    def promjena_brzine_x_za_iznos_dv(self,dv):
        self.set_initial_conditions(self.lista_brzina_x[0]+dv,self.lista_polozaja_x[0],self.lista_polozaja_y[0])
    def __move(self,dt=0.1):
        dax=0
        day=0
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_akceleracija_x.append(self.lista_akceleracija_x[-1]+dax)
        self.lista_akceleracija_y.append(self.lista_akceleracija_y[-1]+day)
        self.lista_brzina_x.append(self.lista_brzina_x[-1]+self.lista_akceleracija_x[-1]*dt)
        self.lista_brzina_y.append(self.lista_brzina_y[-1]+self.lista_akceleracija_y[-1]*dt)
        self.lista_brzina.append(np.sqrt(self.lista_brzina_x[-1]**2+self.lista_brzina_y[-1]**2))
        self.lista_polozaja_x.append(self.lista_polozaja_x[-1]+self.lista_brzina_x[-1]*dt)
        self.lista_polozaja_y.append(self.lista_polozaja_y[-1]+self.lista_brzina_y[-1]*dt)
    def liste(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        return(
        self.lista_vremena,
        self.lista_akceleracija_x,
        self.lista_akceleracija_y,
        self.lista_brzina_x,
        self.lista_brzina_y,
        self.lista_brzina,
        self.lista_polozaja_x,
        self.lista_polozaja_y)
    def plot_x_y(self,dt=0.01):
        (a,b,c,d,e,f,g,h)=self.liste(dt)
        plt.plot(g,h)
        plt.show()
    def plot_vy_t(self,dt=0.01):
        (a,b,c,d,e,f,g,h)=self.liste(dt)
        plt.plot(a,e)
        plt.show()
    def total_time(self,dt=0.01):
        (a,b,c,d,e,f,g,h)=self.liste(dt)
        return (a[-1])
    def total_time_dt(self,dt):
        (a,b,c,d,e,f,g,h)=self.liste(dt)
        return (dt,a[-1])
    def plot_total_time_dt(self,dt1,dt2,ddt):
        lista_dt=[]
        lista_total_time=[]
        while dt1<=dt2:
            (a,b)=self.total_time_dt(dt1)
            lista_dt.append(a)
            lista_total_time.append(b)
            self.set_initial_conditions(self.lista_brzina_x[0],self.lista_polozaja_x[0],self.lista_polozaja_y[0])
            dt1+=ddt
        plt.plot(lista_dt,lista_total_time)
        plt.show()
    def range(self,dt=0.01):
        (a,b,c,d,e,f,g,h)=self.liste(dt)
        return (g[-1])
    def time_to_hit_target(self,xm,r,vv,dt=0.1):
        lista_vremena_bacanja_za_pogodak=[]
        t=0
        m=1
        self.promjena_brzine_x_za_iznos_dv(vv)
        while m!=0:
            self.set_initial_conditions(self.lista_brzina_x[0],self.lista_polozaja_x[0],self.lista_polozaja_y[0],t)
            if ((xm-r) <= (self.range(dt)+(self.lista_brzina_x[0]-vv)*t) and (self.range(dt)+(self.lista_brzina_x[0]-vv)*t) <= (xm+r)):
                lista_vremena_bacanja_za_pogodak.append(t)
            if (self.range(dt)+(self.lista_brzina_x[0]-vv)*t > xm+r):
                m=0
            t+=dt
        return(lista_vremena_bacanja_za_pogodak)

