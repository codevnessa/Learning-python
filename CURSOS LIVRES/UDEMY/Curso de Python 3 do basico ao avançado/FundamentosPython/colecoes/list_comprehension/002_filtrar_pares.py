# Criando uma lista apenas com números pares
pares = [x for x in range(5) if x % 2 == 0]

# Exibindo a lista
print(pares)  # Resultado: [0, 2, 4]

# 1. `[x for x in range(5) if x % 2 == 0]` filtra apenas números pares.
# 2. `x % 2 == 0` verifica se o número é par.
# 3. `print(pares)` exibe a lista.