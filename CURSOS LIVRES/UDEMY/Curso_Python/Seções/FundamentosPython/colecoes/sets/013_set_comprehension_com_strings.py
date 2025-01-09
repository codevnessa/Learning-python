# Usa set comprehension com strings para criar um conjunto de caracteres únicos

# Criando um conjunto de caracteres únicos de uma string
texto = "abracadabra"
caracteres_unicos = {letra for letra in texto}

# Exibindo o conjunto
print(caracteres_unicos)

"""
- texto = "abracadabra": Definindo uma string.
- caracteres_unicos = {letra for letra in texto}: Criando um conjunto com caracteres únicos da string.
- print(caracteres_unicos): Exibe o conjunto de caracteres únicos.
"""