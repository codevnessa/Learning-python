# Uso: quando as classes precisam interagir, mas não há uma relação de posse 
# ou dependência forte, como no exemplo abaixo, onde a classe Escritor pode 
# utilizar diferentes ferramentas para escrever, mas não possui uma relação 
# de dependência forte com nenhuma delas. Isso permite que o Escritor possa 
# trocar de ferramenta (FerramentaDeEscrever) sem que isso afete sua funcionalidade principal


# Classe que representa um escritor
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome  # O nome do escritor
        self._ferramenta = None  # A ferramenta que ele usa (começa sem nada)

    # Propriedade para acessar a ferramenta
    @property
    def ferramenta(self):
        return self._ferramenta

    # Método para definir ou trocar a ferramenta
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


# Classe que representa uma ferramenta para escrever
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome  # O nome da ferramenta

    # Método que simula a ação de escrever
    def escrever(self):
        return f'{self.nome} está escrevendo'


# Cria um escritor chamado "Luiz"
escritor = Escritor('Luiz')

# Cria duas ferramentas: uma caneta e uma máquina de escrever
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

# Define que o escritor vai usar a máquina de escrever
escritor.ferramenta = maquina_de_escrever

# Mostra o que cada ferramenta faz
print(caneta.escrever())  # A caneta escreve
print(maquina_de_escrever.escrever())  # A máquina escreve

# Mostra o que o escritor está fazendo com a ferramenta que ele está usando
print(escritor.ferramenta.escrever())