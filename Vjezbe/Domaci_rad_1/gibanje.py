import particle as prt
import numpy as np
import matplotlib.pyplot as plt
p1=prt.particle()
print(p1.velocity_to_hit_target(0,0,np.pi/6,100,10,4))
print(p1.angle_to_hit_target(0,0,100,10,15,5,0.1,0.1))
p1.graf_domet_kut(0,0,10,0.01)
p1.graf_ukupno_vrijeme_kut(0,0,10,0.01)

