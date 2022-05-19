import Projectile as prt
import numpy as np
import matplotlib.pyplot as plt
def F1(p,Cd,A,v):
    return(-0.5*p*Cd*A*v**2)
p1=prt.Projectile()
p1.set_initial_conditions(100,np.pi/6,0,0,0.1,1,5,F1,'sfera',0.2)
p1.plot_trajectory(0.01)
p1.reset()
p1.set_initial_conditions(100,np.pi/6,0,0,0.1,1,5,F1,'kocka',0.2)
p1.plot_trajectory(0.01)
p1.reset()
plt.show()
p1.set_initial_conditions(100,np.pi/6,0,0,0.1,1,5,F1,'sfera',0.2)
p1.plot_trajectory_rk(0.01)
p1.reset()
p1.set_initial_conditions(100,np.pi/6,0,0,0.1,1,5,F1,'kocka',0.2)
p1.plot_trajectory_rk(0.01)
plt.show()
