def pravac_kroz_2_tocke_graf(x1,y1,x2,y2):
    from numpy import linspace
    import matplotlib.pyplot as plt
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    x=linspace(x1,x2,500)
    plt.plot(x1,y1,marker='o', markerfacecolor='blue', markersize=10)
    plt.plot(x2,y2,marker='o', markerfacecolor='blue', markersize=10)
    plt.plot(x,k*x+l)
    a=int(input('Odaberite unosom znamenke: 1 Prikaz grafa , 2 Spremanje grafa u obliku PDF-a: '))
    if a==1:
        plt.show()
    if a==2:
        b=str(input('Unesite naziv PDF-a: '))
        plt.savefig(b)
pravac_kroz_2_tocke_graf(1,3,2,4)