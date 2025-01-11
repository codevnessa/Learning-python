"""
    O uso do `super()` em Python permite que uma classe filha chame métodos da classe pai, especialmente útil para inicialização e extensão de métodos. Isso ajuda a reutilizar código e manter a lógica da superclasse intacta enquanto adiciona funcionalidades específicas na subclasse.
"""

# Exemplo de uso do super() para inicialização e extensão de métodos

# Classe base (pai)
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Atribui o nome à instância

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}"
        # Método que retorna uma mensagem de apresentação básica

# Classe derivada (filha)
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)  # Chama o __init__ da superclasse para inicializar o nome
        self.curso = curso  # Adiciona um novo atributo específico para Estudante

    def apresentar(self):
        return super().apresentar() + f" e estou estudando {self.curso}"
        # Estende o método `apresentar` da superclasse, adicionando informações sobre o curso

# Uso
estudante = Estudante("João", "Engenharia")  # Cria uma instância de Estudante
print(estudante.apresentar())  # Saída: Olá, meu nome é João e estou estudando Engenharia
                               # Aqui, o método `apresentar` da classe Estudante é chamado, que usa o método da superclasse e adiciona mais informações

"""
- Imagine que você tem uma classe `Pessoa` que sabe se apresentar com o nome.
- Agora, pense em um `Estudante`, que é uma pessoa, mas também tem um curso que está estudando.
- O `super()` é usado para chamar o método da classe `Pessoa` e garantir que o nome seja configurado corretamente.
- Além disso, o método `apresentar` do `Estudante` usa o método da `Pessoa` e adiciona mais informações sobre o curso.
- Isso permite reutilizar o código da `Pessoa` e adicionar funcionalidades específicas do `Estudante` sem repetir código.
"""