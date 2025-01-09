# Como criar uma lista de números usando um loop tradicional e depois usando List Comprehension.

# 1. Criando uma lista com um loop tradicional
lista = []  # Cria uma lista vazia
for numero in range(10):  # Para cada número de 0 a 9
    lista.append(numero)  # Adiciona o número à lista

# Resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Criando a mesma lista usando List Comprehension
lista = [
    numero * 2  # Multiplica cada número por 2
    for numero in range(10)  # Para cada número de 0 a 9
]
print(lista)  # Resultado: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 1. Loop tradicional:
#    - `lista = []`: Cria uma lista vazia.
#    - `for numero in range(10)`: Percorre os números de 0 a 9.
#    - `lista.append(numero)`: Adiciona cada número à lista.
#    - No final, a lista fica assim: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

# 2. List Comprehension:
#    - `lista = [numero * 2 for numero in range(10)]` é uma forma mais curta de criar a lista.
#    - `for numero in range(10)`: