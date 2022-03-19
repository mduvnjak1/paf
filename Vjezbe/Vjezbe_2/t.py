def najveca_brzina(v,alpha,T,dt):
    import numpy as np
    import matplotlib.pyplot as plt
    vx=v*np.cos(alpha)
    vy=v*np.sin(alpha)
    n=round(T/dt)
    t=0
    ax=0
    dax=0
    ay=-10
    day=0
    najveća_brzina=0
    lista_vremena=[t]
    lista_akceleracija_x=[ax]
    lista_akceleracija_y=[ay]
    lista_brzina_x=[vx]
    lista_brzina_y=[vy]
    lista_brzina=[np.sqrt(vx**2+vy**2)]
    for i in range(n):
        t+=dt
        lista_vremena.append(t)
        ax+=dax
        lista_akceleracija_x.append(ax)
        ay+=day
        lista_akceleracija_y.append(ay)
        vx+=ax*dt
        lista_brzina_x.append(vx)
        vy+=ay*dt
        lista_brzina_y.append(vy)
        lista_brzina.append(np.sqrt(vx**2+vy**2))
    for element in lista_brzina:
        if element>najveća_brzina:
            najveća_brzina=element
    print(najveća_brzina)
    print(lista_brzina)
    print(n)
    print(lista_brzina_y)
najveca_brzina(20,1,4,0.01)