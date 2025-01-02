"""
Funções de ordem superior são funções que recebem outras funções como argumentos ou retornam funções.
`*args` pode ser usado em funções de ordem superior para passar um número variável de argumentos para a função recebida.
"""

def aplicar_funcao(funcao, *args):
    """
    Esta função de ordem superior recebe uma função e um número variável de argumentos.
    Ela aplica a função recebida aos argumentos e retorna o resultado.
    """
    return funcao(*args)

resultado = aplicar_funcao(sum, 1, 2, 3, 4, 5)
print(resultado)  # Saída: 15

"""
A função `aplicar_funcao` é uma função de ordem superior que usa `*args` para passar argumentos para a função recebida.
Isso demonstra como `*args` pode ser aplicado em funções de ordem superior para aumentar a flexibilidade e reutilização de código.
"""