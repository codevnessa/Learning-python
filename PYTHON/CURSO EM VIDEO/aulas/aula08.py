from math import sqrt, floor, ceil
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, ceil (raiz)))
print('A raiz de {} é igual a {:.2f}.'.format(num, floor (raiz)))