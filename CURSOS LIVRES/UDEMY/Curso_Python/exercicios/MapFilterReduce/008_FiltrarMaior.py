lista = [1, 4, 9, 16, 25, 36, 49, 64, 81]
maior = list(filter(
    lambda num: num > 20,
    lista
))

print(maior)