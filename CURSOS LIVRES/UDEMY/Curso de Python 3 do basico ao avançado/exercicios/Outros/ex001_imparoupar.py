# Solicita ao usuário que digite um número e armazena o valor na variável 'num'
num = input("DIGITE UM NUMERO: ")

# Verifica se a entrada do usuário é um número inteiro positivo usando o método 'isdigit()'
if num.isdigit():
    # Converte a entrada (que é uma string) para um número inteiro
    num_int = int(num)
    
    # Verifica se o número é par ou ímpar usando o operador módulo (%)
    # Se o resto da divisão por 2 for 0, o número é par; caso contrário, é ímpar
    print("É PAR!" if num_int % 2 == 0 else "NAO É PAR! É IMPAR!")
else:
    # Se a entrada não for um número inteiro positivo, exibe uma mensagem de erro
    print("Voce nao digitou um numero inteiro")
