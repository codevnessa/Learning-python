# Lista original de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criando uma nova lista com números maiores que 5
novo_numeros = [numero for numero in numeros if numero > 5]

# Criando uma lista com números ímpares
impares = [numero for numero in numeros if numero % 2 != 0]

# Criando uma lista com números pares
pares = [numero for numero in numeros if numero % 2 == 0]

# Criando uma lista com uma condição adicional (if-else)
outro_if = [
    numero  # Mantém o número
    if numero != 6 else 600  # Substitui o número 6 por 600
    for numero in pares  # Itera sobre a lista de números pares
]

# Exibindo os resultados
print("Lista Original: \n",numeros)  
print('-'*15)
print("Números maiores que 5: \n",novo_numeros) 
print('-'*15)
print("Números ímpares: \n",impares)
print('-'*15)
print("Números pares: \n",pares)
print('-'*15)
print("Substituicão do 6: \n",outro_if)  # 


"""
    Aplica filtros (if) para selecionar números maiores que 5, ímpares e pares.

    Usa uma expressão condicional (if-else) para substituir o número 6 por 600 na lista de números pares.

    Demonstra como combinar condições e transformações em list comprehensions.
"""