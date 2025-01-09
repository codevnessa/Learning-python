from functools import reduce
lista = [1, 4, 5,3]
multiplicar = reduce(
                lambda y,x: x *y,lista
            )

print(multiplicar)