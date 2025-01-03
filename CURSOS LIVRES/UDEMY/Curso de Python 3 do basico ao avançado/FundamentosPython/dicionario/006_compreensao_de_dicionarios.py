"""
Compreensão de dicionários é uma maneira concisa de criar dicionários a partir de iteráveis.
A sintaxe é semelhante à compreensão de listas, mas com pares chave-valor.
"""

# Exemplo 1: Criar um dicionário a partir de uma lista de tuplas
lista_tuplas = [("a", 1), ("b", 2), ("c", 3)]
dicionario1 = {chave: valor for chave, valor in lista_tuplas}

print("Dicionário 1:", dicionario1)

# Exemplo 2: Criar um dicionário a partir de duas listas
chaves = ["nome", "idade", "cidade"]
valores = ["Alice", 25, "São Paulo"]
dicionario2 = {chaves[i]: valores[i] for i in range(len(chaves))}

print("Dicionário 2:", dicionario2)

# Exemplo 3: Criar um dicionário com condicionais
numeros = [1, 2, 3, 4, 5]
dicionario3 = {n: n**2 for n in numeros if n % 2 == 0}

print("Dicionário 3:", dicionario3)

"""
Explicação:
- No Exemplo 1, criamos um dicionário a partir de uma lista de tuplas, onde cada tupla contém uma chave e um valor.
- No Exemplo 2, criamos um dicionário a partir de duas listas, uma de chaves e outra de valores.
- No Exemplo 3, usamos uma condicional para incluir apenas os números pares no dicionário.

Compreensão de dicionários é uma ferramenta poderosa para criar dicionários de forma concisa e legível.
"""