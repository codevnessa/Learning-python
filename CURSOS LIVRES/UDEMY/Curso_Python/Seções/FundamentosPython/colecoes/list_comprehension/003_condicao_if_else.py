# Criando uma lista com condição e alternativa
numeros = [x if x % 2 == 0 else x * 2 for x in range(5)]

# Exibindo a lista
print(numeros)  # Resultado: [0, 2, 2, 6, 4]

# 1. `[x if x % 2 == 0 else x * 2 for x in range(5)]` mantém pares e dobra ímpares.
# 2. `x if x % 2 == 0 else x * 2` é a condição.
# 3. `print(numeros)` exibe a lista.