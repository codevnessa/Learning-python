# Criando uma sequência com números maiores que 2 e pares
filtrados = [x for x in range(5) if x > 2 and x % 2 == 0]

# Exibindo a sequência
print(filtrados)  # Resultado: [4]

# 1. `[x for x in range(5) if x > 2 and x % 2 == 0]` filtra números maiores que 2 e pares.
# 2. `x > 2 and x % 2 == 0` é a condição.
# 3. `print(filtrados)` exibe a sequência.