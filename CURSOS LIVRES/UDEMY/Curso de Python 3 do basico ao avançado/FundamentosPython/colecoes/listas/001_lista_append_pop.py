# Explicação do conteúdo: O método append() adiciona um elemento ao final da lista, enquanto o método pop() remove e retorna o último elemento ou o elemento em um índice específico.

# Exemplo de uso de append() e pop():
lista = [10, 20, 30]
lista.append(40)  # Adiciona 40 ao final da lista
print("Lista após append:", lista)

elemento_removido = lista.pop()  # Remove e retorna o último elemento
print("Elemento removido:", elemento_removido)
print("Lista após pop:", lista)

# Explicação do código:
# 1. append(40) adiciona o valor 40 ao final da lista.
# 2. pop() remove e retorna o último elemento da lista.
# OBS: pop() também pode receber um índice para remover um elemento específico.