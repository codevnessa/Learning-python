# Usa set comprehension para criar um conjunto de forma concisa, como os quadrados dos números de 0 a 9

# Criando um conjunto com set comprehension
quadrados = {x**2 for x in range(10)}

# Exibindo o conjunto
print(quadrados)

"""
- quadrados = {x**2 for x in range(10)}: Cria um conjunto com os quadrados dos números de 0 a 9.
- print(quadrados): Exibe o conjunto resultante.
"""