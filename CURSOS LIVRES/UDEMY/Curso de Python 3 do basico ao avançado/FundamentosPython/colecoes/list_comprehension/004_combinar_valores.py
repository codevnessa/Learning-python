# Criando uma lista com múltiplos loops
combinacoes = [x + y for x in range(3) for y in range(3)]

# Exibindo a lista
print(combinacoes)  # Resultado: [0, 1, 2, 1, 2, 3, 2, 3, 4]

# 1. `[x + y for x in range(3) for y in range(3)]` combina valores de dois loops.
# 2. `x + y` soma os valores.
# 3. `print(combinacoes)` exibe a lista.