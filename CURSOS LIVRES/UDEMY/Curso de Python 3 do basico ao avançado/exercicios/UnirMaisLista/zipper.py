# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
from itertools import zip_longest

def zipper(lista01,lista02):
    tam = min(len(lista01),len(lista02))
    return [(lista01[i],lista02[i]) for i in range(tam)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']    

   
print(list(zip_longest(l1,l2, fillvalue='Sem cidade')))