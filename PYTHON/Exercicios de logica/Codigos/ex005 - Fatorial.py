# Solicita ao usuário que digite um número
n = int(input("Digite um número: "))

# Inicializa a variável fatorial com 1
fatorial = 1

# Loop para calcular o fatorial do número digitado
for i in range(1, n+1):
    # Multiplica o valor atual de fatorial pelo valor de i
    fatorial *= i

# Exibe o resultado do fatorial
print(f"O fatorial de {n} é {fatorial}")