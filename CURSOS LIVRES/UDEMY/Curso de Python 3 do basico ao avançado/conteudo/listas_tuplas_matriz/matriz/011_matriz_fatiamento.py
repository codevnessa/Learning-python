# Explicação do conteúdo: Podemos extrair submatrizes de uma matriz usando fatiamento (slicing).
# O fatiamento permite selecionar intervalos de linhas e colunas.

# Exemplo de fatiamento de uma matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

submatriz = [linha[1:3] for linha in matriz]  # Extrai as colunas 1 e 2 de todas as linhas
print("Submatriz:", submatriz)

# Explicação do código:
# 1. O fatiamento [1:3] seleciona as colunas 1 e 2 de cada linha.
# OBS: O fatiamento é útil para trabalhar com partes específicas de uma matriz.