def espelhar(matriz):
    espelhado = [linha[::-1] for linha in matriz]
    return espelhado

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

espelhado = espelhar(matriz)

print("MATRIZ ORIGINAL")
for linha in matriz:
    print(f'{' . '.join(map(str,linha))}')
    
print("MATRIZ ESPELHADO")
for linha in espelhado:
    print(f'{' . '.join(map(str,linha))}')

