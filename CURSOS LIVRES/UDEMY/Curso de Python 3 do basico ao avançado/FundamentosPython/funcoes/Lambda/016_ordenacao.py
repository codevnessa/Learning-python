# Funções lambda para ordenar uma lista de forma personalizada.


# Lista de palavras
palavras = ["banana", "maçã", "laranja", "abacaxi"]

# Ordenando as palavras pelo tamanho
ordenadas = sorted(palavras, key=lambda x: len(x))

print(ordenadas)  # Resultado: ['maçã', 'banana', 'laranja', 'abacaxi']

# 1. `sorted(palavras, key=lambda x: len(x))` ordena a lista `palavras`.
# 2. `key=lambda x: len(x)` usa o tamanho de cada palavra como critério de ordenação.
# 3. O resultado é uma lista ordenada pelo tamanho das palavras.