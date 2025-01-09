from datetime import date
# Classe Pessoa com atributo de classe e método para calcular o ano de nascimento
class Pessoa:
    ano_atual = date.today().year 
    
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade  
    def get_ano_nascimento(self):
        # Método para calcular o ano de nascimento usando o atributo de classe
        return Pessoa.ano_atual - self.idade


# Dicionário com dados para criar uma instância de Pessoa
dados = {'nome': 'João', 'idade': 35}

# Criando uma instância de Pessoa usando o dicionário com ** (desempacotamento)
p1 = Pessoa(**dados)

# Exibindo o __dict__ da instância (atributos de instância em formato de dicionário)
print(vars(p1))  # Saída: {'nome': 'João', 'idade': 35}

# Exibindo o valor do atributo 'nome' da instância
print(p1.nome)  # Saída: João