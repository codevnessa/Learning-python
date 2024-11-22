from random import randint
from time import sleep
computador = randint(0,5) #faz o computador pensar no numero
print('=-='*20)
print('Estou pensando em numero de 0 a 5, tente adivinhar...')
print('=-='*20)
jogador = int(input('Qual numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS VOCE ACERTOU!!!')
else:
    print('GANHEI! O numero que eu pensei nao foi {}, foi {}. Infelizmente voce errou :('.format(jogador,computador))
