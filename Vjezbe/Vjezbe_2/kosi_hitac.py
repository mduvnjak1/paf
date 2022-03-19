def putanja_graf(v,alpha,dt):
    import numpy as np
    import matplotlib.pyplot as plt
    vx=v*np.cos(alpha)
    vy=v*np.sin(alpha)
    ax=0
    dax=0
    ay=-9.81
    day=0
    x=0
    y=0
    t=0
    lista_vremena=[t]
    lista_akceleracija_x=[ax]
    lista_akceleracija_y=[ay]
    lista_brzina_x=[vx]
    lista_brzina_y=[vy]
    lista_položaja_x=[x]
    lista_položaja_y=[y]
    while y>=0:
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
        x+=vx*dt
        lista_položaja_x.append(x)
        y+=vy*dt
        lista_položaja_y.append(y)
    plt.plot(lista_položaja_x,lista_položaja_y)
    plt.xlabel('Position x [m]')
    plt.ylabel('Position y [m]')
    plt.show()
def maksimalna_visina(v,alpha,dt):
    import numpy as np
    import matplotlib.pyplot as plt
    vx=v*np.cos(alpha)
    vy=v*np.sin(alpha)
    ax=0
    dax=0
    ay=-9.81
    day=0
    x=0
    y=0
    t=0
    lista_vremena=[t]
    lista_akceleracija_x=[ax]
    lista_akceleracija_y=[ay]
    lista_brzina_x=[vx]
    lista_brzina_y=[vy]
    lista_položaja_x=[x]
    lista_položaja_y=[y]
    while vy>=0:
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
        x+=vx*dt
        lista_položaja_x.append(x)
        y+=vy*dt
        lista_položaja_y.append(y)
    print(lista_položaja_y[-1])
def domet(v,alpha,dt):
    import numpy as np
    import matplotlib.pyplot as plt
    vx=v*np.cos(alpha)
    vy=v*np.sin(alpha)
    ax=0
    dax=0
    ay=-9.81
    day=0
    x=0
    y=0
    t=0
    lista_vremena=[t]
    lista_akceleracija_x=[ax]
    lista_akceleracija_y=[ay]
    lista_brzina_x=[vx]
    lista_brzina_y=[vy]
    lista_položaja_x=[x]
    lista_položaja_y=[y]
    while y>=0:
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
        x+=vx*dt
        lista_položaja_x.append(x)
        y+=vy*dt
        lista_položaja_y.append(y)
    print(lista_položaja_x[-1])
def najveca_brzina(v,alpha,dt,x,y):
    import numpy as np
    import matplotlib.pyplot as plt
    vx=v*np.cos(alpha)
    vy=v*np.sin(alpha)
    t=0
    ax=0
    dax=0
    ay=-9.81
    day=0
    najveća_brzina=0
    lista_vremena=[t]
    lista_akceleracija_x=[ax]
    lista_akceleracija_y=[ay]
    lista_brzina_x=[vx]
    lista_brzina_y=[vy]
    lista_brzina=[np.sqrt(vx**2+vy**2)]
    lista_položaja_x=[x]
    lista_položaja_y=[y]
    while y>=0:
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
        x+=vx*dt
        lista_položaja_x.append(x)
        y+=vy*dt
        lista_položaja_y.append(y)
    for element in lista_brzina:
        if element>najveća_brzina:
            najveća_brzina=element
    print(najveća_brzina)
def meta(v,alpha,dt,xm,ym,r):
    import numpy as np
    import matplotlib.pyplot as plt
    vx=v*np.cos(alpha)
    vy=v*np.sin(alpha)
    ax=0
    dax=0
    ay=-9.81
    day=0
    x=0
    y=0
    t=0
    najmanja_udaljenost=np.sqrt((xm-x)**2+(ym-y)**2)
    lista_vremena=[t]
    lista_akceleracija_x=[ax]
    lista_akceleracija_y=[ay]
    lista_brzina_x=[vx]
    lista_brzina_y=[vy]
    lista_položaja_x=[x]
    lista_položaja_y=[y]
    lista_udaljenosti_do_mete=[np.sqrt((xm-x)**2+(ym-y)**2)]
    while x<=xm:
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
        x+=vx*dt
        lista_položaja_x.append(x)
        y+=vy*dt
        lista_položaja_y.append(y)
        lista_udaljenosti_do_mete.append(np.sqrt((xm-x)**2+(ym-y)**2))
    if (lista_položaja_y[-1]<ym+r and ym-r<lista_položaja_y[-1]):
        print ('Meta je pogođena')
    else:
        while y>=0:
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
            x+=vx*dt
            lista_položaja_x.append(x)
            y+=vy*dt
            lista_položaja_y.append(y)
            lista_udaljenosti_do_mete.append(np.sqrt((xm-x)**2+(ym-y)**2))
        for element in lista_udaljenosti_do_mete:
            if element>najmanja_udaljenost:
                najmanja_udaljenost=element
        print ('Meta nije pogođena')
        print(najmanja_udaljenost)
    plt.plot(lista_položaja_x,lista_položaja_y)
    plt.plot([xm,xm],[ym-r,ym+r],'k-')
    plt.xlabel('Position x [m]')
    plt.ylabel('Position y [m]')
    plt.show()
