# Metodos em instancias de classes Python
# Hard coded - é algo que foi escrito diretamente no codigo

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celca')
print(celta.nome)
celta.acelerar()