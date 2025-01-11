# A sobrecarga de membros ocorre quando uma subclasse define um método ou atributo com o mesmo nome de um método ou atributo da superclasse. 
# Isso significa que a subclasse "substitui" o comportamento original da superclasse. 
# Quando você chama esse método ou acessa esse atributo a partir de uma instância da subclasse, o que será executado ou retornado é o que foi definido na subclasse, e não o da superclasse.

# Definindo a superclasse Veiculo
class Veiculo:
    def __init__(self, marca):
        self.marca = marca  # Atributo comum a todos os veículos

    def descricao(self):
        return f"Veículo da marca {self.marca}"  # Método que descreve o veículo

# Definindo a subclasse Carro, que herda de Veiculo
class Carro(Veiculo):
    def descricao(self):
        # Sobrescrevendo o método descricao da superclasse Veiculo
        return f"Carro da marca {self.marca}"

# Instanciando a subclasse Carro
meu_carro = Carro(marca="Toyota")

# Chamando o método descricao da instância meu_carro
print(meu_carro.descricao())  # Saída: "Carro da marca Toyota"

# Resumo:
# 1. Sobrecarga de membros: A subclasse Carro redefine o método descricao da superclasse Veiculo.
# 2. Substituição do comportamento: Quando chamamos meu_carro.descricao(), o método da classe Carro é executado, retornando "Carro da marca Toyota".
# 3. Personalização: A subclasse pode adaptar o comportamento herdado da superclasse às suas necessidades específicas.
# 4. Utilidade: A sobrecarga de membros permite que as subclasses tenham comportamentos específicos, mantendo a estrutura e organização do código.