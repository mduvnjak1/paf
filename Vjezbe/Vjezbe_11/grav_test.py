import grav as G
import numpy as np
import matplotlib.pyplot as plt
def F1(g1,g2,G=6.67*10**-11):
    return(G*g1.m*g2.m*(g2.xyz-g1.xyz)/np.abs(g2.xyz-g1.xyz)**3)
g1=G.Planet()
g1.set_initial_conditions(np.array((150*10**9,0,0)),np.array((0,30*10**3,0)),6*10**24)
g2=G.Planet()
g2.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),2*10**30)
G.plot_trajectory(g1,g2,F1,10**6)