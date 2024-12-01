num = int(input('Digite um numerode 0 a 9999:'))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000% 10
print('Analisando o número {}, temos as seguintes informações:'.format(num))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))
