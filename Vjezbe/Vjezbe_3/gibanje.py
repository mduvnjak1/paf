import particle as prt
import numpy as np
p1=prt.particle()
p1.set_initial_conditions(10,np.pi/3,0,0)
print(p1.range())
print(p1.domet_analiticki())
p1.plot_trajectory()
print(p1.error())