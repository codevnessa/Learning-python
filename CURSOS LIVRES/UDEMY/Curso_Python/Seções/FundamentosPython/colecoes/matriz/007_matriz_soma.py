# Explicação do conteúdo: A soma de duas matrizes de mesma dimensão é obtida somando os elementos correspondentes.
# Podemos usar list comprehension para realizar a soma.

# Exemplo de soma de duas matrizes:
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

soma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Soma das matrizes:", soma)

# Explicação do código:
# 1. A list comprehension soma os elementos correspondentes das duas matrizes.
# OBS: As matrizes devem ter a mesma dimensão para a soma ser válida.