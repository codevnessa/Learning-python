# Explicação do conteúdo: Tuplas podem ser usadas como chaves em dicionários e para retornar múltiplos valores de funções.
# Isso ocorre porque tuplas são imutáveis e, portanto, podem ser hasheadas.

# Exemplo de tupla como chave de dicionário:
coordenadas = {(10.5, 20.3): "São Paulo", (15.7, 25.8): "Rio de Janeiro"}
print("Cidade nas coordenadas (10.5, 20.3):", coordenadas[(10.5, 20.3)])

# Exemplo de tupla como retorno de função:
def min_max_soma(numeros):
    return min(numeros), max(numeros), sum(numeros)

resultado = min_max_soma([10, 20, 30])
print("Mínimo, máximo e soma:", resultado)

# Explicação do código:
# 1. A tupla (10.5, 20.3) é usada como chave em um dicionário.
# 2. A função min_max_soma retorna três valores em uma tupla.
# OBS: Tuplas são ideais para retornar múltiplos valores de funções de forma organizada.