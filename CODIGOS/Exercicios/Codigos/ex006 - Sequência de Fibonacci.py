# Solicita ao usuário que digite um número
n = int(input("Digite um número: "))

# Inicializa os primeiros dois números da sequência de Fibonacci
a, b = 0, 1

# Loop para gerar e exibir os primeiros n números da sequência de Fibonacci
for _ in range(n):
    # Exibe o valor atual de a
    print(a, end=" ")
    # Atualiza os valores de a e b para os próximos números da sequência
    a, b = b, a + b