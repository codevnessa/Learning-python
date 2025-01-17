def removeDuplicata(lista):
    return list(dict.fromkeys(lista))

lista = [3, 5, 2, 3, 8, 5, 1, 2, 9]
lista_ = removeDuplicata(lista)
ordenada = sorted(lista_)

print(f'Lista original:\n{", ".join(map(str, lista))}')
print()
print(f'Lista sem duplicados:\n{", ".join(map(str, lista_))}')
print()
print('Lista ordenada:')
print(f'{", ".join(map(str, ordenada))}')