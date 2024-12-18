distancia = float(input('Qual a distancia da viajem? '))
p1 = distancia * 0.45
p2 = distancia * 0.50
if distancia <= 200:
    print('A sua viajem de {}km, custará R${:.2f}.'.format(distancia, distancia * 0.50))
else:
    print('A sua viajem de {}km, custará R${:.2f}.'.format(distancia, distancia * 0.45))
print('Obrigada pela preferencia!!!')