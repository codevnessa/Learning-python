"""
- __new__: Esse método é responsável por criar o objeto. Ele é chamado antes de __init__. O __new__ recebe a classe (cls) como argumento e deve retornar o objeto recém-criado. Normalmente, __new__ é usado em casos onde você precisa controlar como a instância é criada (por exemplo, para implementar padrões de design como o Singleton).

- __init__: Esse método é chamado após o objeto ser criado pelo __new__. Ele é responsável por inicializar a instância, ou seja, definir os valores iniciais dos atributos. O __init__ recebe a instância (self) como argumento e não deve retornar nada (deve retornar None implicitamente).

- object: Em Python, a classe base padrão para todas as classes é a classe object. Ou seja, se você não especificar uma classe base ao definir sua classe, ela automaticamente herda de object.
"""
class Pessoa:
    # Método especial __new__: é chamado antes de criar o objeto
    def __new__(cls, *args, **kwargs):
        print("Criando o objeto...") 
        obj = super().__new__(cls)  
        print("Durante a criação do objeto!") 
        return obj  
    
    # Método especial __init__: é chamado após o objeto ser criado, para inicializá-lo
    def __init__(self, nome, idade):
        print("Inicializando a instância...")  
        self.nome = nome 
        self.idade = idade  

# Criando uma instância da classe Pessoa
p = Pessoa("Vanessa", 21)  

print(p.nome, p.idade)  

# Mensagem final
print("\nFim da inicialização")  