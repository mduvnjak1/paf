import harmonic_oscillator as ho
import matplotlib.pyplot as plt
ho1=ho.HarmonicOscillator()
ho1.set_initial_conditions(3,2,10,5)
print(ho1.period(0.5))
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
print(ho1.period(0.1))
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
print(ho1.period(0.01))
ho1.reset()

ho1.set_initial_conditions(3,2,10,5)
ho1.a_t_graf(0.5)
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
ho1.a_t_graf(0.1)
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
ho1.a_t_graf(0.01)
ho1.reset()
plt.show()

ho1.set_initial_conditions(3,2,10,5)
ho1.v_t_graf(0.5)
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
ho1.v_t_graf(0.1)
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
ho1.v_t_graf(0.01)
ho1.reset()
plt.show()

ho1.set_initial_conditions(3,2,10,5)
ho1.x_t_graf(0.5)
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
ho1.x_t_graf(0.1)
ho1.reset()
ho1.set_initial_conditions(3,2,10,5)
ho1.x_t_graf(0.01)
ho1.reset()
plt.show()