import universe as U
import numpy as np
import matplotlib.pyplot as plt
def F1(g1,g2,G=6.67408*10**(-11)):
    return(G*10**(-3)*g1.m*g2.m*(g2.xyz-g1.xyz)/(absv(g2.xyz-g1.xyz))**3)
def absv(v):
    return(np.sqrt(np.dot(v,v)))
Sun=U.Planet()
Earth=U.Planet()
Sun.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1.989*10**6)
Earth.set_initial_conditions(np.array((148.6,0,0)),np.array((0,29.783*10**(-6),0)),5.9742)
lista_objekata=[Sun,Earth]
U.plot_trajectory_rk(lista_objekata,F1)
plt.show()