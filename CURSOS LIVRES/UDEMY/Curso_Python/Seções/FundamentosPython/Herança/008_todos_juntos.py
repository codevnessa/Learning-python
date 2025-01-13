"""
1. **Herança**: Uma classe herda atributos e métodos de outra.
2. **super()**: Usado para chamar métodos da superclasse.
3. **MRO (Method Resolution Order)**: Define a ordem em que as classes são processadas em herança múltipla.
4. **Sobrecarga de métodos**: Uma subclasse redefine um método da superclasse.
5. **Herança múltipla**: Uma classe herda de mais de uma classe base.
"""

# Superclasse base
class Animal:
    def __init__(self, nome):
        self.nome = nome
        print(f"Animal {self.nome} inicializado")
        # Inicializa o atributo 'nome' e imprime uma mensagem

    def fazer_som(self):
        return "Som genérico de animal"
        # Método que retorna um som genérico

    def comer(self):
        return f"{self.nome} está comendo"
        # Método que descreve o animal comendo

# Subclasse que herda de Animal
class Mamifero(Animal):
    def __init__(self, nome, tipo_pelo):
        super().__init__(nome)  # Chama o __init__ da superclasse Animal
        self.tipo_pelo = tipo_pelo
        print(f"Mamífero {self.nome} com pelo {self.tipo_pelo} inicializado")
        # Inicializa o atributo 'tipo_pelo' e imprime uma mensagem

    def fazer_som(self):
        return "Som genérico de mamífero"
        # Sobrecarga do método 'fazer_som' para mamíferos

    def amamentar(self):
        return f"{self.nome} está amamentando"
        # Método específico para mamíferos

# Outra subclasse que herda de Animal
class Ave(Animal):
    def __init__(self, nome, tipo_bico):
        super().__init__(nome)  # Chama o __init__ da superclasse Animal
        self.tipo_bico = tipo_bico
        print(f"Ave {self.nome} com bico {self.tipo_bico} inicializado")
        # Inicializa o atributo 'tipo_bico' e imprime uma mensagem

    def fazer_som(self):
        return "Som genérico de ave"
        # Sobrecarga do método 'fazer_som' para aves

    def voar(self):
        return f"{self.nome} está voando"
        # Método específico para aves

# Classe com herança múltipla (Mamifero e Ave)
class Morcego(Mamifero, Ave):
    def __init__(self, nome, tipo_pelo, tipo_bico):
        # Usando super() para inicializar corretamente as superclasses
        super().__init__(nome=nome, tipo_pelo=tipo_pelo)
        # Ave não é chamada diretamente aqui, pois super() segue o MRO
        self.tipo_bico = tipo_bico
        print(f"Morcego {self.nome} com bico {self.tipo_bico} inicializado")
        # Inicializa o atributo 'tipo_bico' e imprime uma mensagem

    def fazer_som(self):
        # Sobrecarga do método fazer_som
        som_mamifero = super().fazer_som()  # Chama o método da superclasse Mamifero
        return f"{som_mamifero}, mas também emite sons ultrassônicos"
        # Estende o método 'fazer_som' para incluir sons ultrassônicos

    def dormir(self):
        return f"{self.nome} está dormindo de cabeça para baixo"
        # Método específico para morcegos

# Uso do código
morcego = Morcego(nome="Batman", tipo_pelo="curto", tipo_bico="afiado")
# Cria uma instância de Morcego

# Acessando métodos e atributos
print(morcego.fazer_som())  # Saída: Som genérico de mamífero, mas também emite sons ultrassônicos
print(morcego.amamentar())  # Saída: Batman está amamentando
print(morcego.voar())       # Saída: Batman está voando
print(morcego.dormir())     # Saída: Batman está dormindo de cabeça para baixo
print(morcego.comer())      # Saída: Batman está comendo

# Verificando o MRO (Method Resolution Order)
print(Morcego.mro())
# Saída: [<class '__main__.Morcego'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]

"""
- A classe `Animal` é a superclasse base, com métodos genéricos como `fazer_som` e `comer`.
- As classes `Mamifero` e `Ave` herdam de `Animal` e adicionam métodos específicos, como `amamentar` e `voar`.
- A classe `Morcego` herda de `Mamifero` e `Ave` (herança múltipla) e usa `super()` para garantir que os métodos das superclasses sejam chamados na ordem correta (definida pelo MRO).
- O método `fazer_som` é sobrecarregado em cada classe para fornecer comportamentos específicos.
- O MRO define a ordem de resolução de métodos, garantindo que o Python saiba qual método chamar em caso de conflito.
- Isso permite combinar funcionalidades de várias classes de forma organizada e previsível.
"""