# Criando uma lista vazia
lista = []

# Usando dois loops for aninhados para adicionar tuplas à lista
for x in range(3):  # Loop externo: x varia de 0 a 2
    for y in range(3):  # Loop interno: y varia de 0 a 2
        lista.append((x, y))  # Adiciona uma tupla (x, y) à lista

# O resultado será: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Agora, fazendo a mesma coisa usando list comprehension
lista = [
    (x, y)  # Cria uma tupla (x, y)
    for x in range(3)  # Loop externo: x varia de 0 a 2
    for y in range(3)  # Loop interno: y varia de 0 a 2
]

# O resultado será o mesmo: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Agora, criando uma lista de listas de tuplas
lista = [
    [(x, letra) for letra in 'Luiz']  # List comprehension interna: cria tuplas (x, letra)
    for x in range(3)  # Loop externo: x varia de 0 a 2
]

# O resultado será:
# [
#   [(0, 'L'), (0, 'u'), (0, 'i'), (0, 'z')],
#   [(1, 'L'), (1, 'u'), (1, 'i'), (1, 'z')],
#   [(2, 'L'), (2, 'u'), (2, 'i'), (2, 'z')]
# ]

# Exibindo a lista final
print(lista)