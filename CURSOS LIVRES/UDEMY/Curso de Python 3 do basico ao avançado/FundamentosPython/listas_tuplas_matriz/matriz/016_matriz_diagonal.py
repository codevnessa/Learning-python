# Explicação do conteúdo: A diagonal principal de uma matriz é composta pelos elementos onde o índice da linha é igual ao índice da coluna.
# Podemos extrair a diagonal principal usando list comprehension.

# Exemplo de extração da diagonal principal:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

diagonal = [matriz[i][i] for i in range(len(matriz))]
print("Diagonal principal:", diagonal)

# Explicação do código:
# 1. A list comprehension extrai os elementos onde o índice da linha é igual ao índice da coluna.
# OBS: A diagonal principal só existe em matrizes quadradas.