# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
# Definindo a classe CallMe
class CallMe:
    # Método __init__ é o construtor da classe
    def __init__(self, phone):
        self.phone = phone

    # Método __call__ permite que a instância da classe seja "chamada" como uma função
    # Isso significa que podemos usar os parênteses () na instância
    def __call__(self, nome):
        # Imprimindo uma mensagem com o nome e o número de telefone
        print(f"{nome} está chamando o telefone: {self.phone}")
        # Retornando uma mensagem de confirmação
        return f"Chamada realizada para {nome}"

# Criando uma instância da classe CallMe
# Passamos o número de telefone "1234-5678" para o construtor
call_um = CallMe("1234-5678")

# Chamando a instância como se fosse uma função
# Passamos o nome "Vanessa" como argumento
resultado = call_um("Vanessa")

print(resultado)

"""
Esse código mostra como você pode usar o método __call__ para fazer com que uma instância de uma classe seja executável, ou seja, possa ser chamada como uma função. Isso é útil em várias situações, especialmente quando você quer que um objeto execute uma ação específica quando "chamado".
"""