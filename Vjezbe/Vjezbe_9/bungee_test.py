import bungee as bng
import numpy as np
import matplotlib.pyplot as plt
def F1(p,Cd,A,k,x0,l,v,x):
    if np.abs(x-x0)>l:
            xe=x-l
    else:
            xe=0
    return(-0.5*p*Cd*A*v**2-k*xe)
b1=bng.Projectile()
b1.set_initial_conditions(0, 100, 0.3, 10, 0.5, 80, 100, 50, F1)
b1.plot_y_t(100, 0.1)
#p1.reset()
#p1.set_initial_conditions(100,np.pi/6,0,0,0.3,5,1,10,F1)
#p1.plot_trajectory_rk(0.01)
plt.show()
