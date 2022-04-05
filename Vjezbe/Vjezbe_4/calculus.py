import matplotlib.pyplot as plt
import math
def der(func,x,dx=0.01,m=3):
    if m==3:
        return((func(x+dx)-func(x-dx))/(2*dx))
    if m==2:
        return((func(x+dx)-func(x))/dx)

def der_lista(func,a,b,dx=0.01,m=3):
    lista_tocki=[a]
    lista_derivacija=[der(func,a,dx,m)]
    while a<b:
        a+=dx
        lista_tocki.append(a)
        lista_derivacija.append(der(func,a,dx,m))
    return(lista_tocki,lista_derivacija)

def der_po_koraku_plot(func,a,b,dx=0.01,m=3):
    x,dfx=der_lista(func,a,b,dx,m)
    plt.scatter(x,dfx)

def integral(func,a,b,N):
    dx=(b-a)/N
    lista_tocki=[a]
    donja_meda=[func(a)*dx]
    gornja_meda=[func(a+dx)*dx]
    for i in range(N-1):
        a+=dx
        lista_tocki.append(a)
        donja_meda.append(donja_meda[-1]+func(a)*dx)
        gornja_meda.append(gornja_meda[-1]+func(a+dx)*dx)
    return(donja_meda[-1],gornja_meda[-1])

def integral_trapez(func,a,b,N):
    dx=(b-a)/N
    lista_tocki=[a]
    lista_povrsina=[(func(a)+func(b))*dx/2]
    for i in range(N-1):
        a+=dx
        lista_tocki.append(a)
        lista_povrsina.append(lista_povrsina[-1]+(func(a))*dx)
    return(lista_povrsina[-1])

def integral_po_koraku_plot(func,a,b,N):
    dm,gm=integral(func,a,b,N)
    plt.scatter(N,dm)
    plt.scatter(N,gm)

def integral_trapez__po_koraku_plot(func,a,b,N):
    I=integral_trapez(func,a,b,N)
    plt.scatter(N,I)

  