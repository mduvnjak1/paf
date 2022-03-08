def pravac_kroz_2_točke(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    print('y=',k,'x +',l)
pravac_kroz_2_točke(2,4,3,5)