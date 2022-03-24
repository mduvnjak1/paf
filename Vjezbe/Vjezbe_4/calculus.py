import matplotlib.pyplot as plt
import math
def der3(func,x,h):
    return((func(x+h)-func(x-h))/(2*h))

def der2(func,x,h):
    return((func(x+h)-func(x))/h)

def f1(x):
    return(3*x**2)

def der3_lista(func,a,b,dx):
    lista_tocki=[a]
    lista_derivacija=[der3(func,a,dx)]
    for i in range(round((b-a)/dx)):
        a+=dx
        lista_tocki.append(a)
        der3(func,a,dx)
        lista_derivacija.append(der3(func,a,dx))
    print(lista_tocki)
    print(lista_derivacija)

def der2_lista(func,a,b,dx):
    lista_tocki=[a]
    lista_derivacija=[der2(func,a,dx)]
    for i in range(round((b-a)/dx)):
        a+=dx
        lista_tocki.append(a)
        der2(func,a,dx)
        lista_derivacija.append(der2(func,a,dx))
    print(lista_tocki)
    print(lista_derivacija)

def der3_plot(func,a,b,dx):
    lista_tocki=[a]
    lista_derivacija=[der3(func,a,dx)]
    for i in range(round((b-a)/dx)):
        a+=dx
        lista_tocki.append(a)
        der3(func,a,dx)
        lista_derivacija.append(der3(func,a,dx))
    plt.plot(lista_tocki, lista_derivacija)

def der2_plot(func,a,b,dx):
    lista_tocki=[a]
    lista_derivacija=[der2(func,a,dx)]
    for i in range(round((b-a)/dx)):
        a+=dx
        lista_tocki.append(a)
        der2(func,a,dx)
        lista_derivacija.append(der2(func,a,dx))
    plt.plot(lista_tocki, lista_derivacija)
    