def parimpar(*args):
    pares = []
    impares = []
    for numeros in args:
        if numeros % 2 == 0:
            pares.append(numeros)
        else:
            impares.append(numeros)
    return  list(zip(pares, impares))

numeros = list(range(1,50))
resultado = parimpar(*numeros)

for par,impar in resultado:
    print(f'Par: {par}   ||   Impar: {impar}')
print('=-'*20)
print('=-'*9 + "FIM" + '=-'*9 + '-')
print('=-'*20)
