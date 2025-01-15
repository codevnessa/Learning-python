# Função que define a representação personalizada
def repr_(self):
    class_name = self.__class__.__name__ 
    class_dict = self.__dict__  
    class_repr = f'{class_name}({class_dict})'  
    return class_repr

# Decorador para adicionar a função `repr_` como método `__repr__` da classe
def adicionar_repr(cls):
    cls.__repr__ = repr_  
    return cls  #

# Decorador para modificar o comportamento do método `falar`
def decorador_(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)  
        
        if 'Terra' in resultado or 'Brasil' in resultado: 
            return 'Você está em casa!'  
        return resultado  
    return interno

# Classe Pais com o decorador `adicionar_repr`
@adicionar_repr
class Pais:
    def __init__(self, nome):
        self.nome = nome  
        
    @decorador_ 
    def falar(self):
        return f'O Pais é {self.nome}'  
# Classe Planeta com o decorador `adicionar_repr` e método decorado com `decorador_`
@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome 

    @decorador_  
    def falar(self):
        return f'O Planeta é {self.nome}'  
# Uso
br = Pais('Brasil')  
japao = Pais('Japao') 

terra = Planeta('Terra')  
marte = Planeta('Marte')  
print(br.falar())  
print(japao.falar())  
print()
print(terra.falar())  
print(marte.falar())  
"""
- O decorador `adicionar_repr` adiciona uma representação personalizada (`__repr__`) às classes `Pais` e `Planeta`, mostrando o nome da classe e seus atributos.
- O decorador `decorador_` modifica o método `falar` da classe `Planeta` para incluir uma mensagem especial ("Você está em casa!") se o planeta for "Terra".
- Quando você chama `falar` em uma instância de `Planeta`, o decorador verifica se o planeta é "Terra" e retorna a mensagem especial. Caso contrário, retorna o resultado original.
- Isso demonstra como decoradores podem ser usados para adicionar funcionalidades de forma modular e reutilizável.
"""