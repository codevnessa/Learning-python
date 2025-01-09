"""
`OrderedDict` é uma subclasse de `dict` que mantém a ordem em que os itens são inseridos.
A partir do Python 3.7, os dicionários padrão também mantêm a ordem de inserção, mas `OrderedDict` oferece funcionalidades adicionais.
"""

from collections import OrderedDict

# Criando um OrderedDict
dicionario_ordenado = OrderedDict()

dicionario_ordenado["banana"] = 3
dicionario_ordenado["maçã"] = 1
dicionario_ordenado["laranja"] = 2

print("OrderedDict:", dicionario_ordenado)
print()

# Movendo um item para o final
dicionario_ordenado.move_to_end("banana")

print("OrderedDict após mover 'banana' para o final:\n", dicionario_ordenado)
print()

# Movendo um item para o início
dicionario_ordenado.move_to_end("maçã", last=False)

print("OrderedDict após mover 'maçã' para o início:\n", dicionario_ordenado)
print()

"""
Explicação:
- `OrderedDict` mantém a ordem de inserção dos itens, assim como os dicionários padrão a partir do Python 3.7.
- `OrderedDict` oferece métodos adicionais, como `move_to_end()`, que permite mover um item para o final ou para o início do dicionário.
- `OrderedDict` é útil quando a ordem de inserção é importante e você precisa de funcionalidades adicionais de ordenação.
"""