"""
Em Python, a tipagem dinâmica permite que `*args` aceite argumentos de qualquer tipo.
No entanto, em contextos onde a tipagem é importante, como em funções anotadas, é possível usar type hints para indicar os tipos esperados.
"""

def concatenar(*args: str) -> str:
    """
    Esta função recebe um número variável de argumentos do tipo `str` e os concatena.
    A anotação `*args: str` indica que todos os argumentos devem ser strings.
    """
    return ''.join(args)

resultado = concatenar("Hello", " ", "World")
print(resultado)  # Saída: Hello World

"""
A função `concatenar` usa type hints para garantir que todos os argumentos sejam strings.
Isso demonstra como `*args` pode ser combinado com tipagem para aumentar a clareza e a segurança do código.
"""