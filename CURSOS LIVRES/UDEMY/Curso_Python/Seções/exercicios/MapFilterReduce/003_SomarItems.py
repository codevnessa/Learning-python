from functools import reduce

lista = [12,75,89,65,41,36,25]
soma = reduce(
    lambda num1, num2: 
    num1 + num2,
    lista
)


print(soma)