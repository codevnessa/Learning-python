# Explicação do conteúdo: Tuplas possuem métodos úteis, como count() e index().
# count() retorna o número de vezes que um valor aparece na tupla.
# index() retorna o índice da primeira ocorrência de um valor.

# Exemplo de uso dos métodos count() e index():
tupla = (10, 20, 30, 20, 40)
print("Número de vezes que 20 aparece:", tupla.count(20))  # Conta ocorrências de 20
print("Índice da primeira ocorrência de 20:", tupla.index(20))  # Encontra o índice de 20

# Explicação do código:
# 1. O método count(20) retorna quantas vezes o valor 20 aparece na tupla.
# 2. O método index(20) retorna o índice da primeira ocorrência do valor 20.
# OBS: Se o valor não existir na tupla, index() gera um erro.