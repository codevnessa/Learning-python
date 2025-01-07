# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_interator(interador):
    print(*list(interador), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'] ,
]



separador = ( '='*40)
# Gera todas as combinações possíveis de 3 pessoas (a ordem não importa)
print(separador)
print('COMBINATIONS')
print(separador)

print_interator(combinations(pessoas, 3))

print(separador)
print('PERMUTATION')
print(separador)
# Gera todas as permutações possíveis de 3 pessoas (a ordem importa)
print_interator(permutations(pessoas, 3))

print(separador)
print('PRODUCT')
print(separador)
# Gera o produto cartesiano de todas as listas em "camisetas" (considera ordem e repete valores únicos)
print_interator(product(*camisetas))
print('-'*20)
print(separador)
