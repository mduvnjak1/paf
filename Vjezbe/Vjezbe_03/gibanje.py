import particle as prt
import numpy as np
import matplotlib.pyplot as plt
p1=prt.particle()
p1.set_initial_conditions(10,np.pi/6,0,0)
print(p1.range())
p1.reset()
p1.set_initial_conditions(10,np.pi/6,0,0)
print(p1.domet_analiticki())
p1.reset()
p1.set_initial_conditions(10,np.pi/6,0,0)
p1.plot_trajectory()
p1.reset()
p1.set_initial_conditions(10,np.pi/3,0,0)
p1.error_dt_graf(10,np.pi/6,0,0)
print(p1.velocity_to_hit_target(0,0,np.pi/6,100,10,4))
print(p1.angle_to_hit_target(0,0,100,10,15,5,0.1,0.1))
p1.graf_domet_kut(0,0,10,0.01)
p1.graf_ukupno_vrijeme_kut(0,0,10,0.01)

