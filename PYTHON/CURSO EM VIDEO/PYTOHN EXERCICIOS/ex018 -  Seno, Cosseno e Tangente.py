import math
an = float(input('Digite o angulo que deseja: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan (math.radians(an))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s,c,t))
