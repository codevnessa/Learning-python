# Função que define a representação personalizada
def repr_(self):
    class_name = self.__class__.__name__ 
    class_dict = self.__dict__  
    class_repr = f'{class_name}({class_dict})'  
    return class_repr

# Decorador para adicionar a função `repr_`
def adicionar_repr(cls):
    cls.__repr__ = repr_  # Adiciona a função `repr_` como método `__repr__` da classe
    return cls

# Classe Time com o decorador `adicionar_repr`
@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome  

# Classe Planeta com o decorador `adicionar_repr`
@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome  

# Uso
br = Time('Brasil') 
japao = Time('Japao')  

terra = Planeta('Terra') 
marte = Planeta('Marte') 

print(br)  # Saída: Time({'nome': 'Brasil'})
print(japao)  # Saída: Time({'nome': 'Japao'})

print(terra)  # Saída: Planeta({'nome': 'Terra'})
print(marte)  # Saída: Planeta({'nome': 'Marte'})

"""
- A função `repr_` cria uma representação personalizada de um objeto, mostrando o nome da classe e seus atributos.
- O decorador `adicionar_repr` adiciona essa função como método `__repr__` a qualquer classe que o utilize.
- As classes `Time` e `Planeta` usam o decorador, ganhando automaticamente uma representação personalizada.
- Quando você imprime uma instância dessas classes, o método `__repr__` é chamado, exibindo uma string informativa sobre o objeto.
- Isso torna o código mais limpo e reutilizável, pois a funcionalidade de representação é centralizada no decorador.
"""