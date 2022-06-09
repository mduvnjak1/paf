import comet as U
import numpy as np
import matplotlib.pyplot as plt
def F1(g1,g2,G=6.67408*10**(-11)):
    return(G*g1.m*g2.m*(g2.xyz-g1.xyz)/(np.linalg.norm(g2.xyz-g1.xyz))**3)

Sun=U.Planet("Sun")
Mercury=U.Planet("Mercury")
Venus=U.Planet("Venus")
Earth=U.Planet("Earth")
Mars=U.Planet("Mars")
Halley=U.Planet("Halley")

Sun.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1.989*10**30,696340*10**3)
Mercury.set_initial_conditions(np.array((57.9*10**9,0,0)),np.array((0,47.4*10**(3),0)),0.33*10**24,2439.7*10**3)
Venus.set_initial_conditions(np.array((108.2*10**9,0,0)),np.array((0,35*10**(3),0)),4.87*10**24,6051.8*10**3)
Earth.set_initial_conditions(np.array((149.6*10**9,0,0)),np.array((0,29.783*10**(3),0)),5.9742*10**24,6371*10**3)
Mars.set_initial_conditions(np.array((228*10**9,0,0)),np.array((0,24.1*10**(3),0)),0.642*10**24,3389.5*10**3)
Halley.set_initial_conditions(np.array((150*10**9,0,0)),np.array((-20*10**(3),15*10**(3),0)),3*10**14,10*10**3)
lista_objekata=[Sun, Mercury, Venus, Earth, Mars, Halley]
U.universe_plot_trajectory(lista_objekata,F1)
plt.show()

Sun=U.Planet("Sun")
Mercury=U.Planet("Mercury")
Venus=U.Planet("Venus")
Earth=U.Planet("Earth")
Mars=U.Planet("Mars")
Halley=U.Planet("Halley")

Sun.set_initial_conditions(np.array((0,0,0)),np.array((0,0,0)),1.989*10**30,696340*10**3)
Mercury.set_initial_conditions(np.array((57.9*10**9,0,0)),np.array((0,47.4*10**(3),0)),0.33*10**24,2439.7*10**3)
Venus.set_initial_conditions(np.array((108.2*10**9,0,0)),np.array((0,35*10**(3),0)),4.87*10**24,6051.8*10**3)
Earth.set_initial_conditions(np.array((149.6*10**9,0,0)),np.array((0,29.783*10**(3),0)),5.9742*10**24,6371*10**8)
Mars.set_initial_conditions(np.array((228*10**9,0,0)),np.array((0,24.1*10**(3),0)),0.642*10**24,3389.5*10**3)
Halley.set_initial_conditions(np.array((151*10**9,0,0)),np.array((-20*10**(3),30*10**(3),0)),3*10**14,10*10**3)
lista_objekata=[Sun, Mercury, Venus, Earth, Mars, Halley]
U.universe_animate_trajectory(lista_objekata,F1)