from itertools import zip_longest

lista01 = [1, 2, 3, 4, 5, 6, 7]
lista02 = [1, 2, 3, 4]

numeros = list(zip_longest(lista01, lista02, fillvalue=None))

for numero in numeros:
    if None not in numero:
        resultado = numero[0] + numero[1]
        print(resultado)