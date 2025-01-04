# Usa set comprehension com uma condição para filtrar elementos, como números pares

# Criando um conjunto com números pares
pares = {x for x in range(10) if x % 2 == 0}

# Exibindo o conjunto
print(pares)

"""
- pares = {x for x in range(10) if x % 2 == 0}: Cria um conjunto com números pares de 0 a 9.
- print(pares): Exibe o conjunto resultante.
"""