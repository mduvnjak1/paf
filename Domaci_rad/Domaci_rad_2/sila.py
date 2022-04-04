import numpy as np
import matplotlib.pyplot as plt
class sila:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_m=[]
        self.lista_akceleracija=[]
        self.lista_brzina=[]
        self.lista_polozaja=[]
        self.F=0
    def set_initial_conditions(self,x,v,m,F):
        self.lista_vremena.append(0)
        self.lista_m.append(m)
        self.lista_brzina.append(v)
        self.lista_polozaja.append(x)
        self.lista_akceleracija.append(F(self.lista_polozaja[-1],self.lista_brzina[-1],self.lista_vremena[-1])/self.lista_m[-1])
        self.F=F
    def reset(self):
        self.__init__()
    def __move(self,dt=0.1):
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina.append(self.lista_brzina[-1]+self.lista_akceleracija[-1]*dt)
        self.lista_polozaja.append(self.lista_polozaja[-1]+self.lista_brzina[-1]*dt)
        self.lista_akceleracija.append(self.F(self.lista_polozaja[-1],self.lista_brzina[-1],self.lista_vremena[-1])/self.lista_m[-1])
    def a_t_graf(self,dt=0.1,T=10):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_akceleracija)
    def v_t_graf(self,dt=0.01,T=10):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_brzina)
    def x_t_graf(self,dt=0.01,T=10):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_polozaja)