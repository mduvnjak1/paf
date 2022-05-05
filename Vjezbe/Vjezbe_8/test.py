import projectile as prt
import numpy as np
import matplotlib.pyplot as plt
def F1(p,Cd,A,v):
    return(-0.5*p*Cd*A*v**2)
p1=prt.Projectile()
p1.set_initial_conditions(20,np.pi/6,0,0,1,10,1,10,F1)
p1.plot_trajectory(0.01)
p1.reset()
p1.set_initial_conditions(20,np.pi/6,0,0,1,10,1,10,F1)
p1.plot_trajectory_rk(0.01)
plt.show()
