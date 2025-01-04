# Criando uma lista de tuplas com condições e transformações
linhas_e_colunas = [
    (x, y)  # Cria uma tupla (x, y)
    if y != 2 else (x, y * 1000)  # Se y for 2, substitui y por y * 1000

    for x in range(1, 11)  # Loop externo: x varia de 1 a 10
    for y in range(1, 6)  # Loop interno: y varia de 1 a 5
    if x != 2  # Filtra apenas os valores de x diferentes de 2

]
# Exibindo a lista resultante
print(linhas_e_colunas)

"""
    Gera uma lista de tuplas (x, y), onde:
        - y = 2 é substituído por y * 1000.
        - Todas as tuplas onde x = 2 são excluídas.
    Demonstra como combinar múltiplos loops, filtros e transformações em uma única list comprehension.
"""