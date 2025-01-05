# Exemplo de uso de dir, hasattr e getattr em Python

# Definindo uma string e o nome de um método que queremos verificar
string = 'Luiz'  # String de exemplo
metodo = 'strip'  # Nome do método que queremos verificar e executar

# Verifica se o objeto 'string' possui o atributo/método especificado em 'metodo'
if hasattr(string, metodo):
    # Se o método existir, imprime uma mensagem indicando que ele existe
    print('Existe strip')  # Indica que o método 'strip' está disponível na string

    # Usa getattr para acessar o método 'strip' dinamicamente e o executa
    # getattr(string, metodo) retorna o método 'strip', e os parênteses () executam o método
    print(getattr(string, metodo)())  # Executa o método strip() na string 'Luiz'
else:
    # Se o método não existir, imprime uma mensagem indicando que ele não existe
    print('Não existe o método', metodo)  # Indica que o método não está disponível

# - hasattr(objeto, 'nome_do_atributo_ou_metodo'):
#   Verifica se o objeto possui um atributo ou método com o nome especificado.
#   Retorna True se existir, False caso contrário.
#
# - getattr(objeto, 'nome_do_atributo_ou_metodo'):
#   Retorna o atributo ou método do objeto com o nome especificado.
#   Se o atributo/método não existir, levanta uma exceção AttributeError.
#   Pode ser usado para acessar métodos ou atributos dinamicamente.
#
# - dir(objeto):
#   Retorna uma lista de todos os atributos e métodos disponíveis no objeto.
#   Útil para inspecionar o que um objeto pode fazer.
#
# - hasattr(string, 'strip') verifica se a string possui o método 'strip'.
# - getattr(string, 'strip')() acessa e executa o método 'strip' na string.
# - O método strip() remove espaços em branco no início e no final da string.
#   Como a string 'Luiz' não tem espaços extras, o resultado será 'Luiz'.