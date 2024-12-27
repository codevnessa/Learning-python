# Explicação do conteúdo: O método index() retorna o índice do primeiro elemento com o valor especificado, enquanto o método count() retorna o número de vezes que um valor aparece na lista.

# Exemplo de uso de index() e count():
lista = [10, 20, 30, 20, 40]
indice = lista.index(20)  # Retorna o índice do primeiro 20
print("Índice do primeiro 20:", indice)

contagem = lista.count(20)  # Conta quantas vezes 20 aparece na lista
print("Número de vezes que 20 aparece:", contagem)

# Explicação do código:
# 1. index(20) retorna o índice da primeira ocorrência do valor 20.
# 2. count(20) retorna o número de vezes que o valor 20 aparece na lista.
# OBS: index() gera um erro se o valor não existir na lista.