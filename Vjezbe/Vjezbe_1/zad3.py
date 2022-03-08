x1=float(input('Unesite x kordinatu prve točke: '))
y1=float(input('Unesite y kordinatu prve točke: '))
x2=float(input('Unesite x kordinatu druge točke: '))
y2=float(input('Unesite y kordinatu druge točke: '))
k=(y2-y1)/(x2-x1)
l=y1-k*x1
print('y=',k,'x +',l)


