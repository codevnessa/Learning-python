# Define a função mdc que calcula o Máximo Divisor Comum (MDC) de dois números
def mdc(a, b):
    # Loop enquanto b for diferente de 0
    while b != 0:
        # Atualiza a e b usando o algoritmo de Euclides
        a, b = b, a % b
    # Retorna o MDC
    return a

# Solicita ao usuário que digite o primeiro número
a = int(input("Digite o primeiro número: "))

# Solicita ao usuário que digite o segundo número
b = int(input("Digite o segundo número: "))

# Calcula e exibe o MDC dos dois números
print(f"O MDC de {a} e {b} é {mdc(a, b)}")