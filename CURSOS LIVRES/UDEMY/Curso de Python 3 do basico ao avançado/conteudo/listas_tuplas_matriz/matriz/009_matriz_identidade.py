# Explicação do conteúdo: Uma matriz identidade é uma matriz quadrada onde os elementos da diagonal principal são 1 e os demais são 0.
# Podemos criar uma matriz identidade usando list comprehension.

# Exemplo de criação de uma matriz identidade:
n = 3  # Tamanho da matriz (n x n)
identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Matriz identidade:", identidade)

# Explicação do código:
# 1. A list comprehension cria uma matriz onde os elementos da diagonal principal são 1 e os outros são 0.
# OBS: A matriz identidade é útil em operações matemáticas como multiplicação de matrizes.