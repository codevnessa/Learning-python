# Lista original de números
numeros = [1, 2, 3, 4, 5]

# Criando uma nova lista usando list comprehension
novos_numeros = [numero for numero in numeros]

# O código acima é equivalente ao seguinte:
# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

# Alterando o primeiro elemento da lista original
numeros[0] = 20

# Exibindo a nova lista
print(novos_numeros)  # Resultado: [1, 2, 3, 4, 5]
"""
    O código mostra como criar uma nova lista a partir de uma lista existente usando list comprehension.

    A nova lista é uma cópia independente, ou seja, alterações na lista original não afetam a nova lista.

    O uso de list comprehension é mais conciso e eficiente do que um loop tradicional para esse tipo de operação.

"""