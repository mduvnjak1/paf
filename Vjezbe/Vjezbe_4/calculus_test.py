import calculus
import math
import matplotlib.pyplot as plt
import numpy as np
def f1(x):
    return(x**3)
def f2(x):
    return math.sin(x)
calculus.der_plot(f1,0,1,1)
calculus.der_plot(f1,0,1,0.5)
calculus.der_plot(f1,0,1,0.25)
calculus.der_plot(f1,0,1,0.1)
x=np.linspace(0,1,100)
plt.plot(x,3*x**2)
plt.show()
