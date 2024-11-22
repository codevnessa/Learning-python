from time import sleep
print('\033[96m-=\033[m'*20)
casa = float(input('Digite o valor que voce deseja emprestimo mobiliario: R$'))
salario = float(input('Digite seu salario mensal: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prestação = casa/(anos * 12)
print('\033[96m-=\033[m'*20)
sleep(1)
print('Para pagar um emprestimo de R${} em {} anos, a prestação seá de R${:.2f}.!'.format(casa,anos,prestação))
sleep(1)
if (salario * 0.3) >= prestação:
    print('SEU EMPRESTIMO FOI \033[32mAPROVADO\033[m PARABÈNS!!!')
else:
    print('SEU EMPRESTIMO FOI \033[31mNEGADO\033[m!!!')