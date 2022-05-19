import em as em
import numpy as np
import matplotlib.pyplot as plt
def F1(q,E,v,B):
    return(q*E+q*np.cross(v,B))
e1=em.Projectile()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,0,0)), np.array((0,0,0)), np.array((0,1,0)), 0.1, 1, F1)
e1.plot_trajectory()
plt.show()