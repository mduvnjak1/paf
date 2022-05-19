import calculus
import math
import matplotlib.pyplot as plt
import numpy as np
def f1(x):
    return(x**3)
def f2(x):
    return math.sin(x)
calculus.der_po_koraku_plot(f1,0,10,2)
calculus.der_po_koraku_plot(f1,0,10,1)
calculus.der_po_koraku_plot(f1,0,10,0.5)
x=np.linspace(0,10,100)
plt.plot(x,3*x**2)
plt.show()
calculus.der_po_koraku_plot(f2,0,10,2)
calculus.der_po_koraku_plot(f2,0,10,1)
calculus.der_po_koraku_plot(f2,0,10,0.5)
x=np.linspace(0,10,100)
plt.plot(x,np.cos(x))
plt.show()

for N in range(10,200,10):
    calculus.integral_po_koraku_plot(f1,0,10,N)
    calculus.integral_trapez__po_koraku_plot(f1,0,10,N)
y=np.linspace(10,200,200)
plt.plot(y,0*y+2500)
plt.show()
for N in range(10,200,10):
    calculus.integral_po_koraku_plot(f2,0,10,N)
    calculus.integral_trapez__po_koraku_plot(f2,0,10,N)
y=np.linspace(10,200,200)
plt.plot(y,0*y+1-math.cos(10))
plt.show()