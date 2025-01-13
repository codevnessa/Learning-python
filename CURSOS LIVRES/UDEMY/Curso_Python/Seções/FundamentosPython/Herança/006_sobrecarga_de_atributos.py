"""
Sobrecarga de atributos ocorre quando uma classe filha define um atributo com o mesmo nome de um atributo da classe pai. Isso permite que a classe filha "sobrescreva" o valor do atributo da classe pai, sem modificar o original.
"""


# Classe base (pai)
class Pai:
    atributo = "Atributo do Pai"
    # Atributo de classe definido na classe Pai

# Classe derivada (filha)
class Filho(Pai):
    atributo = "Atributo do Filho"
    # Atributo de classe com o mesmo nome, sobrescrevendo o valor da classe Pai

# Uso
pai = Pai()  # Cria uma instância da classe Pai
filho = Filho()  # Cria uma instância da classe Filho

print(pai.atributo)  # Saída: Atributo do Pai
                     # Acessa o atributo da classe Pai

print(filho.atributo)  # Saída: Atributo do Filho
                       # Acessa o atributo da classe Filho, que sobrescreve o da classe Pai

print(Pai.atributo)  # Saída: Atributo do Pai
                     # Acessa o atributo diretamente da classe Pai

print(Filho.atributo)  # Saída: Atributo do Filho
                       # Acessa o atributo diretamente da classe Filho

"""
- A classe `Pai` tem um atributo chamado `atributo` com o valor "Atributo do Pai".
- A classe `Filho` herda de `Pai` e define um atributo com o mesmo nome, mas com um valor diferente: "Atributo do Filho".
- Quando você acessa o atributo em uma instância de `Pai`, ele retorna o valor original.
- Quando você acessa o atributo em uma instância de `Filho`, ele retorna o valor sobrescrito.
- Isso mostra como a classe filha pode "sobrescrever" atributos da classe pai sem afetar o valor original da classe pai.
"""