import numpy as np
import matplotlib.pyplot as plt
class particle:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_akceleracija_x=[]
        self.lista_akceleracija_y=[]
        self.lista_brzina_x=[]
        self.lista_brzina_y=[]
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