# Explicação do conteúdo: O método copy() retorna uma cópia superficial da lista, o operador + concatena duas listas em uma nova lista, e o operador * repete a lista um número específico de vezes.

# Exemplo de uso de copy(), + e *:
lista1 = [10, 20, 30]
lista2 = [40, 50]

copia = lista1.copy()  # Cria uma cópia da lista1
print("Cópia da lista1:", copia)

concatenada = lista1 + lista2  # Concatena lista1 e lista2
print("Lista concatenada:", concatenada)

repetida = lista1 * 2  # Repete lista1 duas vezes
print("Lista repetida:", repetida)

# Explicação do código:
# 1. copy() cria uma cópia superficial da lista.
# 2. O operador + concatena duas listas em uma nova lista.
# 3. O operador * repete a lista um número específico de vezes.
# OBS: copy() é útil para evitar modificar a lista original.