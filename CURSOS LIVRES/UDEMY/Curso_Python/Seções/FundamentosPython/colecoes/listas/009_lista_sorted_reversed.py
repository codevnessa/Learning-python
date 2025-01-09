# Explicação do conteúdo: A função sorted() retorna uma nova lista ordenada (não modifica a lista original), e a função reversed() retorna um iterador com a lista invertida (não modifica a lista original).

# Exemplo de uso de sorted() e reversed():
lista = [30, 10, 20]
ordenada = sorted(lista)  # Retorna uma nova lista ordenada
print("Lista ordenada:", ordenada)

invertida = list(reversed(lista))  # Retorna uma nova lista invertida
print("Lista invertida:", invertida)

# Explicação do código:
# 1. sorted() retorna uma nova lista ordenada sem modificar a original.
# 2. reversed() retorna um iterador que pode ser convertido em uma lista invertida.
# OBS: sorted() e reversed() são úteis quando você não quer modificar a lista original.