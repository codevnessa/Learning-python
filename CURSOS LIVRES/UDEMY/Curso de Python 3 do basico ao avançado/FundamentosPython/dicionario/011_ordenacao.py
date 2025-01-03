"""
Dicionários em Python não mantêm uma ordem específica antes do Python 3.7, mas a partir dessa versão, a ordem de inserção é preservada.
Podemos ordenar dicionários por chave ou valor usando a função `sorted()`.
"""

# Criando um dicionário de exemplo
dicionario = {
    "banana": 3,
    "maçã": 1,
    "laranja": 2
}

# Ordenando por chave
ordenado_por_chave = dict(sorted(dicionario.items()))

print("Ordenado por chave:", ordenado_por_chave)

# Ordenando por valor
ordenado_por_valor = dict(sorted(dicionario.items(), key=lambda item: item[1]))

print("Ordenado por valor:", ordenado_por_valor)

"""
Explicação:
- A função `sorted()` retorna uma lista de tuplas ordenadas. Para converter de volta para um dicionário, usamos `dict()`.
- Para ordenar por chave, usamos `sorted(dicionario.items())`, que ordena as tuplas (chave, valor) por chave.
- Para ordenar por valor, usamos `sorted(dicionario.items(), key=lambda item: item[1])`, onde `item[1]` é o valor.
"""