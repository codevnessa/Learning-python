# Explicação do conteúdo: Uma matriz é triangular inferior se todos os elementos acima da diagonal principal forem zero.
# Podemos verificar isso usando a função all().

# Exemplo de verificação de matriz triangular inferior:
matriz = [[1, 0, 0], [2, 3, 0], [4, 5, 6]]

triangular_inferior = all(matriz[i][j] == 0 for i in range(len(matriz)) for j in range(i+1, len(matriz[0])))
print("A matriz é triangular inferior?", triangular_inferior)

# Explicação do código:
# 1. A função all() verifica se todos os elementos acima da diagonal principal são zero.
# OBS: A matriz deve ser quadrada para ser triangular inferior.