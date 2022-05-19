import numpy as np
import matplotlib.pyplot as plt
class HarmonicOscillator:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_k=[]
        self.lista_m=[]
        self.lista_akceleracija=[]
        self.lista_brzina=[]
        self.lista_polozaja=[]
    def set_initial_conditions(self,v,x,k,m):
        self.lista_vremena.append(0)
        self.lista_k.append(k)
        self.lista_m.append(m)
        self.lista_brzina.append(v)
        self.lista_polozaja.append(x)
        self.lista_akceleracija.append(-k*self.lista_polozaja[-1]/m)
    def reset(self):
        self.__init__()
    def __move(self,dt=0.1):
        self.lista_vremena.append(self.lista_vremena[-1]+dt)
        self.lista_brzina.append(self.lista_brzina[-1]+self.lista_akceleracija[-1]*dt)
        self.lista_polozaja.append(self.lista_polozaja[-1]+self.lista_brzina[-1]*dt)
        self.lista_akceleracija.append(-self.lista_k[-1]*self.lista_polozaja[-1]/self.lista_m[-1])
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
    def period(self,dt=0.01):
        if self.lista_polozaja[0]>=0:
            while self.lista_polozaja[-1]>=0:
                self.__move(dt)
            t1=self.lista_vremena[-1]
            while self.lista_polozaja[-1]<=0:
                self.__move(dt)
            t2=self.lista_vremena[-1]
            T=2*(t2-t1)
        else:
            while self.lista_polozaja[-1]<=0:
                self.__move(dt)
            t1=self.lista_vremena[-1]
            while self.lista_polozaja[-1]>=0:
                self.__move(dt)
            t2=self.lista_vremena[-1]
            T=2*(t2-t1)
        return (T)
