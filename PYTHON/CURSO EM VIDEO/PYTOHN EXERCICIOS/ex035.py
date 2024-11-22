print('=-'*20)
print('ANALIZADOR DE TRIANGULOS')
print('=-'*20)
c1 = float(input('Primeiro numero: '))
c2 = float(input('Segundo numero: '))
c3 = float(input('Terceiro numuro: '))
if c1 == c2 == c3:
    print('ESSE TRIANGULO È EQUILATERO')
if c1 == c2 != c3 and c2 == c3 != c1 and c3 == c1 != c2:
    print ('ESSE TRIANGULO È ISÒCELES')
if c1 != c2 != c3:
    print('ESSE TRIANGULO È ESCALENO')
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Com esses segmentos é possivel fazer um triangulo!')
else:
    print('Com esses segmentos não é possivel fazer um triangulo!')