# Explicação do conteúdo: Uma matriz é simétrica se for igual à sua transposta.
# Podemos verificar a simetria comparando a matriz original com sua transposta.

# Exemplo de verificação de simetria de uma matriz:
matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

transposta = [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]
print("A matriz é simétrica?", matriz == transposta)

# Explicação do código:
# 1. A transposta é criada e comparada com a matriz original.
# OBS: A matriz deve ser quadrada para ser simétrica.