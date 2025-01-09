"""
Em Python, funções são tratadas como objetos de primeira classe, o que significa que elas podem ser atribuídas a variáveis, 
passadas como argumentos para outras funções, retornadas por outras funções, armazenadas em estruturas de dados, 
e até mesmo criadas dinamicamente. Este código demonstra como as funções podem ser atribuídas a variáveis.
"""

# Definindo uma função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Atribuindo a função a uma variável
mensagem = saudacao

# Usando a variável para chamar a função
print(mensagem("Mundo"))

"""
1. A função `saudacao` é definida para receber um argumento `nome` e retornar uma mensagem de saudação.
2. A função `saudacao` é atribuída à variável `mensagem`. Agora, `mensagem` se refere à função `saudacao`.
3. A variável `mensagem` é usada para chamar a função, passando "Mundo" como argumento.
4. O resultado é impresso, mostrando "Olá, Mundo!".

Isso ilustra como funções podem ser tratadas como qualquer outro objeto em Python, permitindo que sejam atribuídas a variáveis.
"""