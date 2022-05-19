import projectile as prt
import numpy as np
import matplotlib.pyplot as plt
def F1(p,Cd,A,v):
    return(-0.5*p*Cd*A*v**2)
p1=prt.Projectile()
p1.set_initial_conditions(100,np.pi/6,0,0,0.3,5,1,10,F1)
p1.plot_trajectory(0.01)
p1.reset()
p1.set_initial_conditions(100,np.pi/6,0,0,0.3,5,1,10,F1)
p1.plot_trajectory_rk(0.01)
plt.show()
p1.graf_domet_Cd(20, np.pi/6, 0, 0, 1, 1, 1, F1, 0.01, 0.01)
p1.graf_domet_masa(20, np.pi/6, 0, 0, 1, 1, 0.3, F1, 0.1, 10, 0.1, 0.01)