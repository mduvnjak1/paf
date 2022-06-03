import numpy as np


def absv(v):
    return(np.sqrt(np.dot(v,v)))
def absvk(v):
    return((v[0]**2+v[1]**2+v[2]**2))

a=np.array((150*(10**9),0,0))
print(np.dot(a,a))
print(absv(a))
print(absvk(a))
print(np.linalg.norm(a))