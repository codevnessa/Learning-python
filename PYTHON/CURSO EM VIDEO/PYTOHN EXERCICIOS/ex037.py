num = int(input('Digite um numero inteiro:'))
binario = bin(num).format(num)[2:]
octal = oct(num)[2:]
hexa = hex(num)[2:]
print('Escolha uma das bases para conversão:')
print('\033[31m[1]\033[m CONVERTE EM BINÁRIO')
print('\033[32m[2]\033[m CONVERTE EM OCTAL')
print('\033[93m[3]\033[m CONVERTE EM HEXADECIMAL')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    print('O número {} convertido para \033[31mBINARIO\033[m resulta em: {}.'.format(num, binario))
elif opcao == 2:
    print('O número {} convertido para \033[32mOCTAL\033[m resulta em: {}.'.format(num,octal))
elif opcao == 3:
    print('O numero {} convertido para \033[93mHEXADECIMAL\033[m resulta em: {}.'.format(num,hexa))
else:
    print('Opção invalida! Tente novamente!')