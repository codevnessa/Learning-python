# Explicação do conteúdo: Uma matriz é triangular superior se todos os elementos abaixo da diagonal principal forem zero.
# Podemos verificar isso usando a função all().

# Exemplo de verificação de matriz triangular superior:
matriz = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]

triangular_superior = all(matriz[i][j] == 0 for i in range(1, len(matriz)) for j in range(i))
print("A matriz é triangular superior?", triangular_superior)

# Explicação do código:
# 1. A função all() verifica se todos os elementos abaixo da diagonal principal são zero.
# OBS: A matriz deve ser quadrada para ser triangular superior.