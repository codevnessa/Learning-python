"""
Ao usar `*args` em funções, é importante documentar claramente o que os argumentos representam.
Isso ajuda outros desenvolvedores a entenderem como a função deve ser usada.
"""

def media(*args):
    """
    Esta função calcula a média de um número variável de argumentos.
    `*args` é uma tupla que contém todos os argumentos passados para a função.
    """
    return sum(args) / len(args)

resultado = media(10, 20, 30)
print(resultado)  # Saída: 20.0

"""
A função `media` é documentada para explicar que ela calcula a média de um número variável de argumentos.
Isso mostra a importância de documentar funções que usam `*args` para garantir clareza e usabilidade.
"""