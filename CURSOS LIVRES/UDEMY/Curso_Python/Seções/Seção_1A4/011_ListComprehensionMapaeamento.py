# Como criar listas usando List Comprehension e como fazer mapeamento de dados (modificar itens de uma lista).


# 1. Criando uma lista com um loop tradicional
lista = []  # Cria uma lista vazia
for numero in range(10):  # Para cada número de 0 a 9
    lista.append(numero)  # Adiciona o número à lista

# Resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista)

# 2. Criando a mesma lista usando List Comprehension
lista = [
    numero * 2  # Multiplica cada número por 2
    for numero in range(10)  # Para cada número de 0 a 9
]
# Resultado: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# print(lista)

# 3. Mapeamento de dados com List Comprehension
# Lista de produtos (cada produto é um dicionário)
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# Aumentando o preço dos produtos em 5% (apenas se o preço for maior que 20)
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumenta o preço em 5%
    if produto['preco'] > 20 else {**produto}  # Se o preço for maior que 20
    for produto in produtos  # Para cada produto na lista de produtos
]

# Exibindo os novos produtos, um por linha
print(*novos_produtos, sep='\n')

# Explicação dentro do código:

# 1. Loop tradicional:
#    - `lista = []`: Cria uma lista vazia.
#    - `for numero in range(10)`: Percorre os números de 0 a 9.
#    - `lista.append(numero)`: Adiciona cada número à lista.
#    - No final, a lista fica assim: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

# 2. List Comprehension:
#    - `lista = [numero * 2 for numero in range(10)]` cria uma lista onde cada número é multiplicado por 2.
#    - O resultado é: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18].

# 3. Mapeamento de dados:
#    - `produtos` é uma lista de dicionários, onde cada dicionário representa um produto com nome e preço.
#    - `novos_produtos` é uma nova lista criada com List Comprehension.
#    - Para cada produto (`for produto in produtos`):
#        - Se o preço do produto for maior que 20 (`if produto['preco'] > 20`):
#            - Aumenta o preço em 5% (`{**produto, 'preco': produto['preco'] * 1.05}`).
#        - Caso contrário (`else`):
#            - Mantém o produto original (`{**produto}`).
#    - O resultado é uma nova lista de produtos, onde apenas os produtos com preço maior que 20 tiveram o preço aumentado.

# 4. Exibindo os resultados:
#    - `print(*novos_produtos, sep='\n')` exibe cada produto em uma linha separada.