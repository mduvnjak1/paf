import numpy as np
import matplotlib.pyplot as plt
class HarmonicOscilator:
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
        plt.show()
    def v_t_graf(self,dt=0.01,T=10):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_brzina)
    def x_t_graf(self,dt=0.01,T=10):
        while self.lista_vremena[-1]<=T:
            self.__move(dt)
        plt.plot(self.lista_vremena,self.lista_polozaja)
 
ho1=HarmonicOscilator()
ho1.set_initial_conditions(3,2,10,5)
ho1.a_t_graf()