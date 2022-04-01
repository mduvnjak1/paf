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
    donja_meda=[func(a-dx)*dx]
    gornja_meda=[func(a+dx)*dx]
    while a<b:
        a+=dx
        lista_tocki.append(a)
        donja_meda.append(donja_meda[-1]+func(a-dx)*dx)
        gornja_meda.append(gornja_meda[-1]+func(a+dx)*dx)
    return(lista_tocki,donja_meda,gornja_meda)

def integral_trapez(func,a,b,N):
    dx=(b-a)/N
    lista_tocki=[a]
    lista_povrsina=[(func(a-dx)+func(a+dx))*dx]
    while a<b:
        a+=dx
        lista_tocki.append(a)
        lista_povrsina.append((lista_povrsina[-1]+(func(a-dx)+func(a+dx))*dx/2))
    return(lista_tocki,lista_povrsina)

def integral_po_koraku_plot(func,a,b,N):
    x,dm,gm=integral(func,a,b,N)
    plt.scatter(x,dm)
    plt.scatter(x,gm)

def integral_trapez__po_koraku_plot(func,a,b,N):
    x,I=integral_trapez(func,a,b,N)
    plt.scatter(x,I)

  