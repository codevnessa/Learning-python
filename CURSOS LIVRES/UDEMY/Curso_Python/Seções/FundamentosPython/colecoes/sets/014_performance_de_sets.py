# Compara a performance de operações de busca em listas e conjuntos, mostrando que conjuntos são mais eficientes

import time

# Criando uma lista e um conjunto com os mesmos elementos
elementos = list(range(1000000))
conjunto = set(elementos)

# Buscando um elemento na lista
inicio = time.time()
999999 in elementos
fim = time.time()
print(f"Tempo de busca na lista: {fim - inicio} segundos")

# Buscando um elemento no conjunto
inicio = time.time()
999999 in conjunto
fim = time.time()
print(f"Tempo de busca no conjunto: {fim - inicio} segundos")

"""
- elementos = list(range(1000000)): Criando uma lista com 1 milhão de elementos.
- conjunto = set(elementos): Convertendo a lista em um conjunto.
- 999999 in elementos: Buscando um elemento na lista e medindo o tempo.
- 999999 in conjunto: Buscando o mesmo elemento no conjunto e medindo o tempo.
- print(...): Exibe os tempos de busca.
"""