# Criando uma sequência de tuplas
tuplas = [(x, x ** 2) for x in range(5)]

# Exibindo a sequência
print(tuplas)  # Resultado: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# 1. `[(x, x ** 2) for x in range(5)]` cria tuplas com números e seus quadrados.
# 2. `(x, x ** 2)` forma as tuplas.
# 3. `print(tuplas)` exibe a sequência.