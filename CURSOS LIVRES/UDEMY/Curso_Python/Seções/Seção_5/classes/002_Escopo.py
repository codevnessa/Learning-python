# Escopo global: a classe Animal é definida no escopo global
class Animal:
    # Escopo da classe: atributos e métodos da classe estão neste escopo
    # (o atributo 'nome' está comentado, então não está em uso)
    # nome = 'Leão'

    # Escopo do método __init__: variáveis aqui são locais ao método
    def __init__(self, nome):
        # self.nome é um atributo da instância (escopo da instância)
        self.nome = nome

        # variavel é uma variável local ao método __init__
        variavel = 'valor'
        print(variavel)  # Acessível apenas dentro deste método

    # Escopo do método comendo: variáveis aqui são locais ao método
    def comendo(self, alimento):
        # self.nome é acessível porque pertence ao escopo da instância
        return f'{self.nome} está comendo {alimento}'

    # Escopo do método executar: variáveis aqui são locais ao método
    def executar(self, *args, **kwargs):
        # Chama o método comendo, passando argumentos
        return self.comendo(*args, **kwargs)


# Escopo global: a instância 'leao' é criada no escopo global
leao = Animal(nome='Leão')

# Acessa o atributo 'nome' da instância 'leao' (escopo da instância)
print(leao.nome)

# Chama o método 'executar' da instância 'leao' (escopo da instância)
print(leao.executar('maçã'))