"""
Em Python, `*args` é uma convenção usada para passar um número variável de argumentos para uma função.
Isso é útil quando você não sabe quantos argumentos serão passados. Funções built-in, como `print`, 
podem aceitar múltiplos argumentos, e `*args` funciona de maneira semelhante.
"""

def soma(*args):
    """
    Esta função recebe um número variável de argumentos usando `*args` e retorna a soma deles.
    `*args` é uma tupla que contém todos os argumentos passados para a função.
    """
    return sum(args)

resultado = soma(1, 2, 3, 4, 5)
print(resultado)  # Saída: 15

"""
A função `soma` aceita qualquer número de argumentos e os soma usando a função built-in `sum`.
Isso demonstra como `*args` pode ser usado para criar funções flexíveis que lidam com um número variável de entradas.
"""