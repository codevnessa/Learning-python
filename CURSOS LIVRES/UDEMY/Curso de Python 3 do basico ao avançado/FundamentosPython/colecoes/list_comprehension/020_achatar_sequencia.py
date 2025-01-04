# Achatando uma sequência de sequências
achatada = [x for sublist in [[1, 2], [3, 4]] for x in sublist]

# Exibindo a sequência
print(achatada)  # Resultado: [1, 2, 3, 4]

# 1. `[x for sublist in [[1, 2], [3, 4]] for x in sublist]` achata a sequência.
# 2. `x` é cada elemento das sub-sequências.
# 3. `print(achatada)` exibe a sequência.