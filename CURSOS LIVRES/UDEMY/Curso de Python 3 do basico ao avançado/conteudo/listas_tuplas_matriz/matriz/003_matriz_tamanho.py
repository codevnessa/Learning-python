# Explicação do conteúdo: O tamanho de uma matriz pode ser obtido usando a função len().
# O número de linhas é o comprimento da matriz, e o número de colunas é o comprimento da primeira linha.

# Exemplo de obtenção do tamanho de uma matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

linhas = len(matriz)  # Número de linhas
colunas = len(matriz[0])  # Número de colunas
print(f"A matriz tem {linhas} linhas e {colunas} colunas.")

# Explicação do código:
# 1. len(matriz) retorna o número de linhas.
# 2. len(matriz[0]) retorna o número de colunas (assumindo que todas as linhas têm o mesmo comprimento).
# OBS: Se a matriz for irregular, o número de colunas pode variar.