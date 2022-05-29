import em as em
import numpy as np
import matplotlib.pyplot as plt
def F1(q,E,v,B):
    return(q*E+q*np.cross(v,B))

def E0(t,T):
    return(np.array((0,0,0)))
def B0(t,T):
    return(np.array((0,0,1)))

def E1(t,T):
    return(np.array((0,0,0)))
def B1(t,T):
    if t<T:
        return(np.array((0,0,t/T)))
    else:
        return(np.array((0,0,1)))

#elektron konstantno polje
fig=plt.figure()
ax = fig.add_subplot(projection='3d')
e1=em.Projectile()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), E0, B0, 1, -1, F1)
e1.plot_trajectory()
e1.reset()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), E0, B0, 1, -1, F1)
e1.plot_trajectory_rk()
e1.reset()
plt.show()


#elektron promjenivo polje
fig=plt.figure()
ax = fig.add_subplot(projection='3d')
e1=em.Projectile()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), E1, B1, 1, -1, F1)
e1.plot_trajectory()
e1.reset()
e1.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), E1, B1, 1, -1, F1)
e1.plot_trajectory_rk()
e1.reset()
plt.show()


#pozitron promjenivo polje
fig=plt.figure()
ax = fig.add_subplot(projection='3d')
e2=em.Projectile()
e2.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), E1, B1, 1, 1, F1)
e2.plot_trajectory()
e2.reset()
e2.set_initial_conditions(np.array((0,0,0)), np.array((10,10,10)), E1, B1, 1, 1, F1)
e2.plot_trajectory_rk()
e2.reset()
plt.show()