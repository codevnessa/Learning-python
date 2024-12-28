# Explicação do conteúdo: Podemos transformar uma matriz em uma lista unidimensional (achatamento) usando list comprehension.
# Isso é útil para processar todos os elementos da matriz como uma única lista.

# Exemplo de achatamento de uma matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

achatada = [elemento for linha in matriz for elemento in linha]
print("Matriz achatada:", achatada)

# Explicação do código:
# 1. A list comprehension percorre todos os elementos da matriz e os coloca em uma única lista.
# OBS: O achatamento é útil para operações que requerem uma lista unidimensional.