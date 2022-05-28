import grav as G
import numpy as np
import matplotlib.pyplot as plt
def F1(g1,g2,G=6.67408*10**(-11)):
    return(G*10**(-3)*g1.m*g2.m*(g2.xyz-g1.xyz)/(absv(g2.xyz-g1.xyz))**3)
def absv(v):
    return(np.sqrt(np.dot(v,v)))
g1=G.Planet()
g2=G.Planet()
g1.set_initial_conditions(np.array((148.6,0,0)),np.array((0,29.783*10**(-6),0)),5.9742)
g2.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1.989*10**6)
G.plot_trajectory(g1,g2,F1)
plt.show()
g1.reset()
g2.reset()
g1.set_initial_conditions(np.array((148.6,0,0)),np.array((0,29.783*10**(-6),0)),5.9742)
g2.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1.989*10**6)
G.plot_trajectory_rk(g1,g2,F1)
plt.show()