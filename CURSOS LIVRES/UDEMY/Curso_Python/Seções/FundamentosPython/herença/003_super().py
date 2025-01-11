# A função super() retorna um objeto proxy que delega chamadas de método para uma classe pai ou irmã seguindo o MRO (Method Resolution Order).

# Classe base (superclasse)
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Atributo comum a todas as pessoas

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}"  # Método para apresentação básica

# Classe derivada (subclasse)
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)  # Chama o construtor da classe base (Pessoa) para inicializar o nome
        self.curso = curso  # Atributo específico de Estudante

    def apresentar(self):
        # Sobrescreve o método da classe base, reutilizando-o com super()
        return f"{super().apresentar()} e eu estudo {self.curso}"

# Instanciando a subclasse
estudante = Estudante(nome="Maria", curso="Engenharia")
print(estudante.apresentar())  # Saída: Olá, meu nome é Maria e eu estudo Engenharia

# Resumo:
# 1. Herança: Estudante herda atributos e métodos de Pessoa, permitindo reutilizar código.
# 2. Sobrecarga de método: Estudante sobrescreve o método 'apresentar' de Pessoa para incluir informações específicas.
# 3. Reutilização de código: super() permite reutilizar o método da classe base, evitando duplicação.
# 4. Utilidade: Facilita a extensão e manutenção do código, promovendo organização e modularidade.