# Descrição: Este código mostra como criar listas usando List Comprehension, fazer mapeamento de dados e aplicar filtros.

# Importando a função pprint para exibir dados de forma mais organizada
import pprint

# Função personalizada para exibir dados de forma bonita
def p(v):
    pprint.pprint(v, sort_dicts=True, width=40)

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

# Exibindo os novos produtos
# print(novos_produtos)
# p(novos_produtos)

# 4. List Comprehension com filtro
# Filtra produtos com preço maior ou igual a 20 e cujo novo preço (com aumento) seja maior que 10
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumenta o preço em 5%
    if produto['preco'] > 20 else {**produto}  # Se o preço for maior que 20
    for produto in produtos  # Para cada produto na lista de produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10  # Filtra os produtos
]

# Exibindo os novos produtos filtrados
p(novos_produtos)