# Explicação do conteúdo: Podemos criar uma cópia independente de uma matriz usando list comprehension.
# Isso evita que modificações na cópia afetem a matriz original.

# Exemplo de cópia de uma matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

copia = [linha[:] for linha in matriz]  # Cria uma cópia independente
print("Cópia da matriz:", copia)

# Explicação do código:
# 1. A list comprehension cria uma nova lista para cada linha da matriz.
# OBS: A cópia é independente, então modificações na cópia não afetam a matriz original.