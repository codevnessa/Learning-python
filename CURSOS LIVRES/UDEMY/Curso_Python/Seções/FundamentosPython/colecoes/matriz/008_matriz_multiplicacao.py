# Explicação do conteúdo: A multiplicação de duas matrizes é realizada multiplicando as linhas da primeira matriz pelas colunas da segunda.
# O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.

# Exemplo de multiplicação de duas matrizes:
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

produto = [[sum(a*b for a, b in zip(linha, coluna)) for coluna in zip(*matriz2)] for linha in matriz1]
print("Produto das matrizes:", produto)

# Explicação do código:
# 1. A list comprehension realiza a multiplicação das linhas de matriz1 pelas colunas de matriz2.
# OBS: O número de colunas de matriz1 deve ser igual ao número de linhas de matriz2.