import numpy as np
class particle:
    def __init__(self):
        self.lista_vremena=[]
        self.lista_akceleracija_x=[]
        self.lista_akceleracija_y=[]
        self.lista_brzina_x=[]
        self.lista_brzina_y=[]
        self.lista_položaja_x=[]
        self.lista_položaja_y=[]
    def set_initial_conditions(self, v, angle, x, y):
        vx=v*np.cos(angle)
        vy=v*np.sin(angle)
        self.lista_vremena.append(0)
        self.lista_akceleracija_x.append(0)
        self.lista_akceleracija_y.append(-9.81)
        self.lista_brzina_x.append(vx)
        self.lista_brzina_y.append(vy)
        self.lista_položaja_x.append(x)
        self.lista_položaja_y.append(y)
    def reset(self):
        self.__init__()
    def __move(self):
        t=self.lista_vremena[0]
        ax=self.lista_akceleracija_x[0]
        ay=self.lista_akceleracija_y[0]
        vx=self.lista_brzina_x[0]
        vy=self.lista_brzina_y[0]
        x=self.lista_položaja_x[0]
        y=self.lista_položaja_y[0]
        dt=0.1
        t+=dt
        ax+=0
        ay+=0
        vx+=ax*dt
        vy+=ay*dt
        x+=vx*dt
        y+=vy*dt
        self.lista_vremena.append(t)
        self.lista_akceleracija_x.append(ax)
        self.lista_akceleracija_y.append(ay)
        self.lista_brzina_x.append(vx)
        self.lista_brzina_y.append(vy)
        self.lista_položaja_x.append(x)
        self.lista_položaja_y.append(y)
    def range(self):
        while self.lista_položaja_y[-1]>=0:
            self.__move()
        print (self.lista_položaja_x[-1])
p1=particle()
p1.set_initial_conditions(10,1,0,0)
p1.range()
