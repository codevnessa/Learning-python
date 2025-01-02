"""
`*args` pode ser usado em funções anônimas (lambda) para aceitar um número variável de argumentos.
Isso é útil quando você precisa de uma função simples e rápida que lida com múltiplos argumentos.
"""

soma = lambda *args: sum(args)

resultado = soma(1, 2, 3, 4, 5)
print(resultado)  # Saída: 15

"""
A função lambda `soma` usa `*args` para aceitar qualquer número de argumentos e retorna a soma deles.
Isso demonstra como `*args` pode ser aplicado em funções anônimas para criar funções flexíveis e concisas.
"""