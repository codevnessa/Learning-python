n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
so = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é :{}\nSua subtraçao {}\nO produto é:{}\nA diivisão é:{:.2f}. '.format(so, sub, m, d), end='')
print('Sua divisão inteira é {}, e sua potencia é {}'.format(di, e))