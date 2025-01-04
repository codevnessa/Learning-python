# String original
string = 'Vanessa'

# Número de letras em cada parte
numero_de_letras = 1

# Criando uma nova string com partes separadas por ponto
nova_string = '_'.join([
    string[indice:indice + numero_de_letras]  # Extrai uma parte da string
    for indice in range(0, len(string), numero_de_letras)  # Itera sobre a string
])

# Exibindo a nova string
print(nova_string)

"""
    - Us list comprehension para iterar sobre a string e extrair as partes.
    - Junta as partes com um ponto (.) usando a função join.
    - O resultado é uma nova string com as partes separadas por pontos.
"""