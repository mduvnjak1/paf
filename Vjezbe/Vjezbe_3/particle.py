import numpy as np
import matplotlib.pyplot as plt
class particle:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_akceleracija_x=[]
        self.lista_akceleracija_y=[]
        self.lista_brzina_x=[]
        self.lista_brzina_y=[]
        self.lista_brzina=[]
        self.lista_polozaja_x=[]
        self.lista_polozaja_y=[]
    def set_initial_conditions(self, v, angle, x, y):
        vx=v*np.cos(angle)
        vy=v*np.sin(angle)
        self.lista_vremena.append(0)
        self.lista_akceleracija_x.append(0)
        self.lista_akceleracija_y.append(-9.81)
        self.lista_brzina_x.append(vx)
        self.lista_brzina_y.append(vy)
        self.lista_brzina.append(v)
        self.lista_polozaja_x.append(x)
        self.lista_polozaja_y.append(y)
    def reset(self):
        self.__init__()
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
    def range(self,dt=0.1):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        return (self.lista_polozaja_x[-1])
    def plot_trajectory(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        plt.plot(self.lista_polozaja_x,self.lista_polozaja_y)
        plt.show()
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
    def total_time(self,dt=0.01):
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        return (self.lista_vremena[-1])
    def max_speed(self,dt=0.01):
        najveća_brzina=0
        while self.lista_polozaja_y[-1]>=0:
            self.__move(dt)
        for element in self.lista_brzina:
            if element>najveća_brzina:
                najveća_brzina=element
        return (najveća_brzina)
    def velocity_to_hit_target(self,x,y,angle,xm,ym,r,dv=0.1,dt=0.01):
        self.lista_brzina_pogotka=[]
        v=0
        m=0
        while m==0:
            v+=dv
            self.set_initial_conditions(v,angle,x,y)
            while self.lista_polozaja_x[-1]<=xm:
                self.move(dt)
            if (self.lista_polozaja_y[-1]<ym+r and ym-r<self.lista_polozaja_y[-1]):
                m=1
                self.lista_brzina_pogotka.append(v)
        while m==1:
            v+=dv
            self.set_initial_conditions(v,angle,x,y)
            while self.lista_polozaja_x[-1]<=xm:
                self.move(dt)
            if (self.lista_polozaja_y[-1]<ym+r and ym-r<self.lista_polozaja_y[-1]):
                self.lista_brzina_pogotka.append(v)
            else:
                m=2
        return([self.lista_brzina_pogotka[1],self.lista_brzina_pogotka[-1]])
    def angle_to_hit_target(self,x,y,v,xm,ym,r,dangle=0.1,dt=0.01):
        self.lista_kuta_pogotka1=[]
        self.lista_kuta_pogotka2=[]
        angle=0
        m=0
        while m==0:
            self.set_initial_conditions(v,angle,x,y)
            while self.lista_polozaja_x[-1]<=xm:
                self.move(dt)
            if (self.lista_polozaja_y[-1]<ym+r and ym-r<self.lista_polozaja_y[-1]):
                m=1
                self.lista_kuta_pogotka1.append(angle)
            angle+=dangle
        while m==1:
            angle+=dangle
            self.set_initial_conditions(v,angle,x,y)
            while self.lista_polozaja_x[-1]<=xm:
                self.move(dt)
            if (self.lista_polozaja_y[-1]<ym+r and ym-r<self.lista_polozaja_y[-1]):
                self.lista_kuta_pogotka1.append(angle)
            else:
                m=2
        while m==2:
            self.set_initial_conditions(v,angle,x,y)
            while self.lista_polozaja_x[-1]<=xm:
                self.move(dt)
            if (self.lista_polozaja_y[-1]<ym+r and ym-r<self.lista_polozaja_y[-1]):
                m=3
                self.lista_kuta_pogotka2.append(angle)
            angle+=dangle
        while m==3:
            angle+=dangle
            self.set_initial_conditions(v,angle,x,y)
            while self.lista_polozaja_x[-1]<=xm:
                self.move(dt)
            if (self.lista_polozaja_y[-1]<ym+r and ym-r<self.lista_polozaja_y[-1]):
                self.lista_kuta_pogotka2.append(angle)
            else:
                m=4
        return([[self.lista_kuta_pogotka1[1],self.lista_kuta_pogotka1[-1]],[self.lista_kuta_pogotka2[1],self.lista_kuta_pogotka2[-1]]])
    def graf_domet_kut(self,x,y,v,dangle=0.1,dt=0.01):
        angle=0
        lista_kuteva=[]
        lista_dometa=[]
        while angle<=1.57:
            self.set_initial_conditions(v,angle,x,y)
            lista_kuteva.append(angle)
            lista_dometa.append(self.range(dt))
            angle+=dangle
        return (lista_kuteva,lista_dometa)
    def graf_ukupno_vrijeme_kut(self,x,y,v,angle,dangle=0.1,dt=0.01):
        angle=0
        lista_kuteva=[]
        lista_ukupnog_vremena=[]
        while angle<=1.57:
            self.set_initial_conditions(v,angle,x,y)
            lista_kuteva.append(angle)
            lista_ukupnog_vremena.append(self.total_time(dt))
            angle+=dangle
        return (lista_kuteva,lista_ukupnog_vremena)

    
