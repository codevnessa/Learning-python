"""
Sobrecarga de métodos (method overriding) é um conceito em programação orientada a objetos onde uma classe filha pode fornecer uma implementação específica de um método que já existe na classe pai. Isso permite que a classe filha altere ou estenda o comportamento do método herdado.
"""

# Exemplo de sobrecarga de métodos (method overriding)

# Classe base (pai)
class Veiculo:
    def mover(self):
        return "O veículo está se movendo"
        # Este é o método original que será sobrescrito na classe filha

# Classe derivada (filha)
class Carro(Veiculo):
    def mover(self):
        return "O carro está andando na estrada"
        # Aqui, o método `mover` é sobrescrito para fornecer uma implementação específica para carros

# Uso
veiculo = Veiculo()  # Criando uma instância da classe Veiculo
carro = Carro()      # Criando uma instância da classe Carro

print(veiculo.mover())  # Saída: O veículo está se movendo
                        # Aqui, o método `mover` da classe Veiculo é chamado

print(carro.mover())    # Saída: O carro está andando na estrada
                        # Aqui, o método `mover` da classe Carro é chamado, que sobrescreve o método da classe Veiculo

"""
- Imagine que você tem um veículo genérico que pode se mover de alguma forma. Isso é representado pela classe `Veiculo`.
- Agora, pense em um carro, que é um tipo específico de veículo. O carro também se move, mas de uma maneira mais específica: ele anda na estrada.
- No código, a classe `Carro` herda da classe `Veiculo` e muda o comportamento do método `mover` para refletir como um carro se move.
- Quando chamamos `mover` em um objeto `Veiculo`, ele usa a implementação genérica. Mas quando chamamos `mover` em um objeto `Carro`, ele usa a implementação específica do carro.
"""