# Definindo uma lista iterável
interable = ['Eu', 'tenho', '__iter__']  # Lista contendo três strings

# Criando um iterador a partir da lista
iterator = iter(interable)  # A função iter() transforma a lista em um iterador

print(next(iterator))
print(next(iterator))  
print(next(iterator))  

# O que acontece se chamarmos next() novamente?
# print(next(iterator))  # Isso geraria um erro: StopIteration
# Como não há mais elementos no iterador, next() levantaria a exceção StopIteration.

# Explicação dos conceitos:
# - Iterável: Um objeto que pode ser percorrido em um loop (como listas, tuplas, strings, etc.).
#   No exemplo, a lista ['Eu', 'tenho', '__iter__'] é um iterável.
#
# - Iterador: Um objeto que permite percorrer um iterável, um elemento de cada vez.
#   A função iter() é usada para criar um iterador a partir de um iterável.
#
# - next(): Função que retorna o próximo elemento de um iterador.
#   Cada chamada de next() avança o iterador para o próximo elemento.
#   Quando não há mais elementos, next() levanta a exceção StopIteration.
#
# No exemplo:
# - iterator = iter(interable) cria um iterador para a lista.
# - next(iterator) é chamado três vezes para acessar os três elementos da lista.
# - Se next() fosse chamado uma quarta vez, geraria um erro, pois não há mais elementos.