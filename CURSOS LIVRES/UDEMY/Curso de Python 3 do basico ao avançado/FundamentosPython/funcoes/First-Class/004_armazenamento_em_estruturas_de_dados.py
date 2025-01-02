# Definindo algumas funções
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

# Armazenando funções em uma lista
operacoes = [somar, subtrair, multiplicar]

# Usando as funções armazenadas na lista
resultado = operacoes[1](10, 5)
print(resultado)

"""
1. Três funções são definidas: `somar`, `subtrair` e `multiplicar`.
2. Essas funções são armazenadas em uma lista chamada `operacoes`.
3. A primeira função na lista (`somar`) é chamada com os argumentos 10 e 5.
4. O resultado da operação (15) é impresso.

Isso ilustra como funções podem ser armazenadas em estruturas de dados, permitindo que sejam acessadas e usadas dinamicamente.
"""