"""
Classes abstratas, conhecidas como Abstract Base Classes (ABCs), são utilizadas como contratos na definição de novas classes, forçando subclasses a implementar métodos concretos específicos. Elas podem conter métodos abstratos, que não possuem corpo e são definidos com o decorator @abstractmethod, além de métodos concretos, com implementação própria. Um aspecto importante das classes abstratas é que elas não podem ser instanciadas diretamente, ou seja, são usadas apenas como base para outras classes.

A criação de classes abstratas em Python é feita utilizando a metaclasse ABCMeta, fornecida pelo módulo abc. Métodos abstratos definidos em uma classe abstrata devem obrigatoriamente ser implementados nas subclasses. Além disso, é possível definir @property, @setter, @classmethod, @staticmethod e métodos normais como abstratos, utilizando @abstractmethod como o decorator mais interno.
"""


from abc import ABC, abstractmethod

# Classe abstrata AbstractFoo
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None  # Atributo privado para armazenar o nome
        self.name = name   # Usa o setter para definir o nome

    @property
    def name(self):
        return self._name
        # Getter para a propriedade name

    @name.setter
    @abstractmethod
    def name(self, name): ...
    # Setter abstrato que deve ser implementado pelas subclasses

# Subclasse concreta Foo
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)  # Chama o __init__ da superclasse

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name
        # Implementação do setter abstrato para a propriedade name

# Uso
foo = Foo('Bar')
print(foo.name)   # Saída: Bar
                  # Acessa a propriedade name, que foi configurada pelo setter

"""
- A classe `AbstractFoo` é uma classe abstrata que define uma propriedade `name` com um getter e um setter abstrato.
- O setter abstrato (`@name.setter`) força as subclasses a implementar como o valor de `name` deve ser atribuído.
- A classe `Foo` implementa o setter abstrato, permitindo que o valor de `name` seja armazenado no atributo privado `_name`.
- Quando você cria uma instância de `Foo` e define o nome, o setter é chamado para armazenar o valor.
- Isso garante que todas as subclasses de `AbstractFoo` implementem a lógica para definir o valor de `name`, seguindo o contrato da classe abstrata.
"""

