# Criando uma lista filtrada
inteiros = [x for x in [1, 'a', 3.14] if isinstance(x, int)]

# Exibindo a lista
print(inteiros)  # Resultado: [1]

# 1. `[x for x in [1, 'a', 3.14] if isinstance(x, int)]` filtra apenas números inteiros.
# 2. `isinstance(x, int)` verifica se x é inteiro.
# 3. `print(inteiros)` exibe a lista.