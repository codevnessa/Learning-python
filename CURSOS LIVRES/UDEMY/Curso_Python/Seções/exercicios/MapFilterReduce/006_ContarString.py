from functools import reduce
lista = ["banana", "maçã", "laranja", "uva", "melancia"]
contar = reduce(lambda acumulador, palavra: acumulador + len(palavra), lista, 0)

print(contar)