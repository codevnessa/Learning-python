# Definindo uma função decoradora que adicionará funcionalidades extras à função passada como argumento.
def funcao(func):
    # Definindo a função interna, que será executada no lugar da função original.
    def interna(*args, **kwargs):
        # Mensagem indicando que a função está sendo decorada.
        print('Vou te decorar')
        
        # Itera sobre todos os argumentos posicionais passados para verificar se são strings.
        for arg in args:
            is_string(arg)
        
        # Chama a função original (que foi passada como argumento) com os mesmos parâmetros.
        resultado = func(*args, **kwargs)
        
        # Mensagem informando o resultado da execução da função original.
        print(f'O seu resultado foi {resultado}')
        
        # Mensagem indicando que a função foi decorada.
        print('Agora voce foi decorada')
        
        # Retorna o resultado da execução da função original.
        return resultado
    
    # Retorna a função interna, que substituirá a função original.
    return interna

# Definindo uma função simples que inverte uma string.
def inverter(string):
    return string[::-1]  # Retorna a string invertida.

# Função auxiliar para verificar se um parâmetro é do tipo string.
def is_string(param):
    # Se o parâmetro não for uma string, levanta um erro de tipo.
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# Aqui, estamos aplicando manualmente o decorador `funcao` à função `inverter`.
# A nova função decorada é atribuída a `checar_parametro`.
checar_parametro = funcao(inverter)

# Chamamos a função decorada com a string '123'.
invertida = checar_parametro('123')

# Exibimos o resultado da função decorada.
print(invertida)
