def divisãoFn(x, y):
    return x / y  # Retorna o resultado da divisão de x por y


def multiplicaçãoFn(x, y):
    return x * y  # Retorna o resultado da multiplicação de x por y


def potenciaçãoFn(x, y):
    return x ** y  # Retorna o resultado de x elevado a y


# Lista original de números
numeros = [1, 2, 3, 4, 5]

divisão = [divisãoFn(numero, 2) for numero in numeros]

multiplicação = [multiplicaçãoFn(numero, 2) for numero in numeros]

quadrado = [potenciaçãoFn(numero, 2) for numero in numeros]

print(numeros)  # Lista original
print(divisão)  # Lista com os números divididos por 2
print(multiplicação)  # Lista com os números multiplicados por 2
print(quadrado)  # Lista com os números elevados ao quadrado

"""
    Usa list comprehension para aplicar essas funções a cada elemento de uma lista (numeros).

    Demonstra como transformar uma lista original em novas listas com valores modificados.

    As novas listas são independentes da lista original.
"""