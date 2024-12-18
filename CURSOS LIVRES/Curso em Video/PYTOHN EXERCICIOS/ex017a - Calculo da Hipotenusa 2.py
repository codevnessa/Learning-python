import math
co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente'))
hi = math.hypot(co, ca)
print('o calculo da hipotenusa é: {:.2f}'.format(hi))