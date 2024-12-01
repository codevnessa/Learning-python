dia = float(input('Por quantos dias o carro foi alugado?'))
km = float (input('Por quantos km rodou o carro:'))
print('Total a pagar é de R${:.2f}.'.format((dia * 60) + (km * 0.15)))
