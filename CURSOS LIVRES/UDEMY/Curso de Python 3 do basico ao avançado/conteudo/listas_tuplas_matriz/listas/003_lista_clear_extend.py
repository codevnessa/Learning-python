# Explicação do conteúdo: O método clear() remove todos os elementos da lista, enquanto o método extend() adiciona todos os elementos de uma lista (ou iterável) ao final da lista atual.

# Exemplo de uso de clear() e extend():
lista = [10, 20, 30]
lista.clear()  # Remove todos os elementos da lista
print("Lista após clear:", lista)

lista.extend([40, 50])  # Adiciona os elementos [40, 50] ao final da lista
print("Lista após extend:", lista)

# Explicação do código:
# 1. clear() remove todos os elementos, deixando a lista vazia.
# 2. extend([40, 50]) adiciona os valores 40 e 50 ao final da lista.
# OBS: extend() é útil para combinar listas sem criar uma nova lista.