# Explicação do conteúdo: O método insert() insere um elemento em uma posição específica, enquanto o método remove() remove o primeiro elemento com o valor especificado.

# Exemplo de uso de insert() e remove():
lista = [10, 20, 30]
lista.insert(1, 15)  # Insere 15 na posição 1
print("Lista após insert:", lista)

lista.remove(20)  # Remove o primeiro 20 da lista
print("Lista após remove:", lista)

# Explicação do código:
# 1. insert(1, 15) insere o valor 15 na posição 1 da lista.
# 2. remove(20) remove o primeiro valor 20 da lista.
# OBS: remove() gera um erro se o valor não existir na lista.