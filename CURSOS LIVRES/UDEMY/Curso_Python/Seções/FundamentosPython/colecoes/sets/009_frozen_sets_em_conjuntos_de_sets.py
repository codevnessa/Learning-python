# Mostra como usar frozen sets dentro de outros conjuntos

# Criando frozen sets
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])

# Criando um conjunto de frozen sets
conjunto_de_frozen_sets = {fs1, fs2}

# Exibindo o conjunto
print(conjunto_de_frozen_sets)

"""
- fs1 = frozenset([1, 2, 3]) e fs2 = frozenset([4, 5, 6]): Criando dois frozen sets.
- conjunto_de_frozen_sets = {fs1, fs2}: Criando um conjunto que contém os frozen sets.
- print(conjunto_de_frozen_sets): Exibe o conjunto de frozen sets.
"""