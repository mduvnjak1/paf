import em as em
import numpy as np
import matplotlib.pyplot as plt
def F1(q,E,v,B):
    return(q*E+q*np.cross(v,B))

#elektron usporedba Eulera i Runge kutta metode
e1=em.Projectile()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, -1, F1)
e1.plot_trajectory()
plt.show()
e1.reset()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, -1, F1)
e1.plot_trajectory_rk()
plt.show()
e1.reset()

#pozitron usporedba Eulera i Runge kutta metode
e2=em.Projectile()
e2.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, 1, F1)
e2.plot_trajectory()
plt.show()
e2.reset()
e2.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, 1, F1)
e2.plot_trajectory_rk()
plt.show()
e2.reset()

#elektron pozitron Euler
e1=em.Projectile()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, -1, F1)
e1.plot_trajectory()
e1.reset()
e2=em.Projectile()
e2.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, 1, F1)
e2.plot_trajectory()
plt.show()
e2.reset()

#elektron pozitron Runge kutta
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, -1, F1)
e1.plot_trajectory_rk()
e1.reset()
e2.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), np.array((0,0,0)), np.array((0,0,1)), 1, 1, F1)
e2.plot_trajectory_rk()
plt.show()
e2.reset()
