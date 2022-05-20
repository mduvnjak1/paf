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
print(p1.angle_to_hit_target(100,0,0,0.1,1,5,F1,'sfera',0.2, 100, 200, 15, 0.05, 0.1))
#for element in p1.angle_to_hit_target(100,np.pi/6,0,0,0.1,1,5,F1,'sfera',0.2, 100, 200, 15, 0.05, 0.1):
    #p=p1=prt.Projectile()
    #p.set_initial_conditions(100,element,0,0,0.1,1,5,F1,'sfera',0.2)
    #p.plot_trajectory(0.01)
    #p.reset()
#plt.plot([100,100],[185,215],'k-')
#plt.show()
