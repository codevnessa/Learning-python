class Carro:
    def __init__(self, nome):
       self.nome = nome
       self._motor = None
       self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
       self.nome = nome

class Fabricante:
    def __init__(self, nome):
       self.nome = nome
       

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor10= Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor10
print(f"Carro: {fusca.nome}")
print(f"Motor: {fusca.motor.nome}")
print(f"Fabricante: {fusca.fabricante.nome}")
print('_'*20)
uno = Carro('UNO')
fiat = Fabricante('Fiat')
motor10= Motor('1.0')
uno.fabricante = fiat
uno.motor = motor10
print(f"Carro: {uno.nome}")
print(f"Motor: {uno.motor.nome}")
print(f"Fabricante: {uno.fabricante.nome}")