import calculus
import math
import matplotlib.pyplot as plt
def f1(x):
    return(x*x-2*x)
def f2(x):
    return math.sin(x)
calculus.der2_plot(f2,0,6.28,0.01)
plt.show()
