import grav as G
import numpy as np
import matplotlib.pyplot as plt
def F1(m1,m2,xyz1,xyz2,G=6.67*10**-11):
    return(G*m1*m2*(xyz2-xyz1)/np.abs(xyz2-xyz1)**3)
F1(1,1,(1,2,3),(4,5,6),1)