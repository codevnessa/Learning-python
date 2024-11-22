from time import sleep
velocidade = float(input('Qual a sua velocidade:'))
multa = (velocidade -80) * 7
sleep(1)
if velocidade > 80:
    print('Você deveria ser mais cuidadoso, passou do limite permitido de 80km/h!Sua multa ficou em R${:.2f}.'.format(multa))
sleep(1)
print('Tenha um bom dia! Dirigir com segurança, protege a vida de muita gente, inclusive a sua!')