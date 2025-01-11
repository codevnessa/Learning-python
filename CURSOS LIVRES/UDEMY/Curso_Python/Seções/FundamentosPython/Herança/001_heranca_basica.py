"""
    Herança é um conceito da programação orientada a objetos que permite que uma classe (chamada de classe filha) herde atributos e métodos de outra classe (chamada de classe mãe ou superclasse)
    
    Isso permite reutilizar código e criar uma hierarquia de classes, onde a classe filha podeter comportamentos específicos além dos que herda da classe mãe
    
    Imagine que você tem uma classe "Animal" que define características gerais de um animal, como fazer som
    
    Agora, se você quiser criar uma classe específica para um cachorro, em vez de reescrever tudo, você pode herdar da classe "Animal" e apenas adicionar ou modificar o que for necessário.
"""


# Classe mãe (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome  # Atributo comum a todos os animais

    def fazer_som(self):
        return "Som genérico de animal"  # Método genérico para fazer som

# Classe filha (subclasse) que herda de Animal
class Gato(Animal):
    def fazer_som(self):
        return "Au Au!"  # Método específico para cachorros

# Uso das classes
animal = Animal("Animal Genérico")  # Criando uma instância da classe Animal
cachorro = Gato("Rex")  # Criando uma instância da classe Cachorro

# Chamando o método fazer_som de cada instância
print(animal.fazer_som())  # Saída: Som genérico de animal
print(cachorro.fazer_som())  # Saída: Au Au!

"""
1. A classe `Animal` é a superclasse, que define um comportamento genérico para todos os animais.
2. A classe `Cachorro` é uma subclasse que herda de `Animal`. Ela reutiliza o atributo `nome` e o método `fazer_som`, mas sobrescreve o método `fazer_som` para retornar um som específico de cachorro.
3. Quando criamos uma instância de `Animal` e chamamos `fazer_som`, ele retorna o som genérico.
4. Quando criamos uma instância de `Cachorro` e chamamos `fazer_som`, ele retorna "Au Au!", porque o método foi sobrescrito na subclasse.

Isso mostra como a herança permite reutilizar código e especializar comportamentos em classes mais específicas.
"""