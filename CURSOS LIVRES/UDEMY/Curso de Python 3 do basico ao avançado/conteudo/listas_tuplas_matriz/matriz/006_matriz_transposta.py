# Explicação do conteúdo: A transposta de uma matriz é obtida trocando suas linhas por colunas.
# Podemos criar a transposta usando list comprehension.

# Exemplo de criação da transposta de uma matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposta = [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]
print("Matriz transposta:", transposta)

# Explicação do código:
# 1. A list comprehension troca as linhas por colunas, criando a transposta.
# OBS: A transposta de uma matriz 3x3 também será 3x3.