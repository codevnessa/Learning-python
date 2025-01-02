"""
`*args` pode ser usado em funções recursivas para passar um número variável de argumentos em cada chamada recursiva.
Isso é útil quando o número de argumentos pode variar em cada nível de recursão.
"""

def fatorial(*args):
    """
    Esta função recursiva calcula o fatorial de um número usando `*args`.
    O primeiro argumento é o número para o qual o fatorial é calculado, e os demais argumentos são ignorados.
    """
    if args[0] == 1:
        return 1
    return args[0] * fatorial(args[0] - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120

"""
A função `fatorial` usa `*args` para aceitar um número variável de argumentos, mas apenas o primeiro argumento é usado.
Isso mostra como `*args` pode ser aplicado em funções recursivas, embora nem todos os argumentos precisem ser utilizados.
"""