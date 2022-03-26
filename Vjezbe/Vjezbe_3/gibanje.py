import particle as prt
import numpy as np
import matplotlib.pyplot as plt
p1=prt.particle()
p1.set_initial_conditions(10,np.pi/6,0,0)
#print(p1.range())
#p1.reset()
#p1.set_initial_conditions(10,np.pi/6,0,0)
#print(p1.domet_analiticki())
#p1.reset()
#p1.set_initial_conditions(10,np.pi/6,0,0)
#p1.plot_trajectory()
#p1.reset()
#p1.set_initial_conditions(10,np.pi/3,0,0)

lista_dt=[]
lista_error=[]
dt=0
for i in range(300):
    dt+=0.01
    lista_dt.append(dt)
    lista_error.append(p1.error(dt))
    p1.reset()
    p1.set_initial_conditions(10,np.pi/3,0,0)
plt.plot(lista_dt,lista_error)
plt.show()

