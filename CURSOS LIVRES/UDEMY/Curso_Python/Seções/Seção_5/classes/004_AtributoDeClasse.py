# Classe Pessoa: demonstra o uso de atributos de classe

from datetime import date
class Pessoa:
    # Método construtor: inicializa atributos de instância (únicos para cada objeto)
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade  

    # Método de instância: calcula o ano de nascimento com base no ano_atual
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


# Criando instâncias da classe Pessoa
p1 = Pessoa('João', 35)  
p2 = Pessoa('Helena', 12) 

# Acessando o atributo de classe diretamente pela classe
print(Pessoa.ano_atual)  


# Calculando e exibindo o ano de nascimento de cada pessoa
print(p1.get_ano_nascimento()) 
print(p2.get_ano_nascimento()) 