import bungee as bng
import numpy as np
import matplotlib.pyplot as plt
def F1(p,Cd,A,k,x0,l,v,x):
    if np.abs(x-x0)>l:
            xe=x-x0+l
    else:
            xe=0
    return(-0.5*p*Cd*A*v**2*np.sign(v)-k*xe)
b1=bng.Projectile()
b1.set_initial_conditions(0, 100, 0, 10, 0.5, 80, 100, 50, F1)
b1.plot_y_t(50,0.01)
b1.reset()
b1.set_initial_conditions(0, 100, 0, 10, 0.5, 80, 100, 50, F1)
b1.plot_y_t_rk(50,0.01)
plt.show()
b1.reset()
#S otporom zraka
b1.set_initial_conditions(0, 100, 0.3, 10, 0.5, 80, 100, 50, F1)
b1.plot_energija_t(100,0.01)
plt.show()
b1.reset()
b1.set_initial_conditions(0, 100, 0.3, 10, 0.5, 80, 100, 50, F1)
b1.plot_energija_t_rk(100,0.01)
plt.show()
b1.reset()
#Bez otpora zraka
b1.set_initial_conditions(0, 100, 0, 10, 0.5, 80, 100, 50, F1)
b1.plot_energija_t(100,0.01)
plt.show()
b1.reset()
b1.set_initial_conditions(0, 100, 0, 10, 0.5, 80, 100, 50, F1)
b1.plot_energija_t_rk(100,0.01)
plt.show()
b1.reset()

