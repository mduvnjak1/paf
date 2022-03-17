def kružnica(x1,y1,p,q,r):
    import numpy as np
    import matplotlib.pyplot as plt
    l=np.linspace(0,2*np.pi,150)
    x=p+r*np.cos(l) 
    y=q+r*np.sin(l)
    plt.plot(x,y)
    plt.plot(x1,y1,marker='o', markerfacecolor='blue', markersize=10)
    if (x1-p)**2+(y1-q)**2<r**2:
        print('Točka se nalazi unutar kružnice')
    elif (x1-p)**2+(y1-q)**2==r**2:
        print('Točka se nalazi na kružnici')
    elif (x1-p)**2+(y1-q)**2>r**2:
        print('Točka se nalazi izvan kružnice')
    d=np.sqrt(np.absolute((x1-p)**2+(y1-q)**2-r**2))
    print ('Udaljenost od točke do kružnice je ', d)
    a=int(input('Odaberite unosom znamenke: 1 Prikaz grafa , 2 Spremanje grafa u obliku PDF-a: '))
    if a==1:
        plt.show()
    if a==2:
        b=str(input('Unesite naziv PDF-a: '))
        plt.savefig(b)
kružnica(5,5,0,0,3)