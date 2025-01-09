# Definindo uma função que retorna outra função
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar
   

# Retornando uma função específica
saudar_ola = criar_saudacao("Olá")

# Usando a função retornada
print(saudar_ola("Mundo"))

"""
1. A função `criar_saudacao` é definida para receber uma string `saudacao` e retornar uma função interna `saudar`.
2. A função interna `saudar` recebe um argumento `nome` e retorna uma mensagem de saudação.
3. `criar_saudacao` é chamada com o argumento "Olá", retornando a função `saudar` configurada para usar "Olá".
4. A função retornada é armazenada na variável `saudar_ola`.
5. `saudar_ola` é chamada com o argumento "Mundo", retornando "Olá, Mundo!".

Isso demonstra como funções podem ser retornadas por outras funções, permitindo a criação de funções especializadas.
"""