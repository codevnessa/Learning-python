# Explicação do conteúdo: Tuplas podem conter outras tuplas (aninhamento) e são imutáveis.
# No entanto, se uma tupla contiver objetos mutáveis (como listas), esses objetos podem ser alterados.

# Exemplo de tupla aninhada e imutabilidade profunda:
tupla = ([1, 2], [3, 4])  # Tupla contendo listas
print("Tupla original:", tupla)

tupla[0].append(3)  # Modifica a lista dentro da tupla
print("Tupla após modificar a lista interna:", tupla)

# Explicação do código:
# 1. A tupla contém duas listas.
# 2. A lista interna é modificada, mas a tupla em si permanece imutável.
# OBS: A imutabilidade das tuplas não se aplica a objetos mutáveis que elas contêm.