# Definindo uma função que recebe outra função como argumento
def aplicar_funcao(funcao, valor):
    return funcao(valor)

# Definindo uma função simples
def dobrar(x):
    return x * 2

# Passando a função `dobrar` como argumento para `aplicar_funcao`
resultado = aplicar_funcao(dobrar, 5)
print(resultado)

"""
1. A função `aplicar_funcao` é definida para receber uma função `funcao` e um valor `valor`.
2. A função `dobrar` é definida para receber um número e retornar o dobro dele.
3. A função `dobrar` é passada como argumento para `aplicar_funcao`, junto com o valor 5.
4. `aplicar_funcao` chama `dobrar` com o valor 5 e retorna o resultado, que é 10.

Isso mostra como funções podem ser passadas como argumentos, permitindo a criação de funções de alta ordem.
"""