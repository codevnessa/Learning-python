# Criando uma função dinamicamente
def criar_funcao_potencia(expoente):
    def potencia(base):
        return base ** expoente
    return potencia

# Criando uma função para elevar ao quadrado
quadrado = criar_funcao_potencia(2)

# Usando a função criada dinamicamente
resultado = quadrado(5)
print(resultado)

"""
1. A função `criar_funcao_potencia` é definida para receber um argumento `expoente` e retornar uma função interna `potencia`.
2. A função interna `potencia` recebe um argumento `base` e retorna `base ** expoente`.
3. `criar_funcao_potencia` é chamada com o argumento 2, retornando a função `potencia` configurada para elevar ao quadrado.
4. A função retornada é armazenada na variável `quadrado`.
5. `quadrado` é chamada com o argumento 5, retornando 25.

Isso ilustra como funções podem ser criadas e manipuladas dinamicamente, permitindo a criação de funções personalizadas em tempo de execução.
"""