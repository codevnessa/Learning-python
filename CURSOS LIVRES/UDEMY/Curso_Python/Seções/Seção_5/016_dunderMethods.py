"""
 `__str__` e `__repr__`  Esses métodos controlam como os objetos são representados como strings, tanto para exibição informal (`__str__`) quanto para exibição formal (`__repr__`). O uso de `!r` e `!s` em f-strings permite escolher explicitamente qual representação usar.
"""

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x 
        self.y = y  
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}'
        # Representação informal (str) - usada por str()e f-strings com !s

    def __repr__(self):
        class_name = type(self).__name__  
        return f'{class_name}(x={self.x}, y={self.y}, z={self.z!r})'
        # Representação formal (repr) - usada por repr() e f-strings com !r

# Uso
p1 = Ponto(1, 2)
p2 = Ponto(978, 876) 

print('__str__')
print(p1)  # Saída: 1, 2 (usa __str__)
print(p2)  # Saída: 978, 876 (usa __str__)
print()

print('__repr__')
print(repr(p1))  # Saída: Ponto(x=1, y=2, z='String') (usa __repr__)
print(repr(p2))  # Saída: Ponto(x=978, y=876, z='String') (usa __repr__)
print()

print('!r - repr')
print(f'{p1!r}')  # Saída: Ponto(x=1, y=2, z='String') (usa __repr__ com !r)
print()

print('!s - str')
print(f'{p1!s}')  # Saída: 1, 2 (usa __str__ com !s)

"""
- A classe `Ponto` representa um ponto com coordenadas x, y e um atributo z (com valor padrão 'String').
- O método `__str__` define como o objeto é exibido de forma informal, como quando você usa `print(p1)`.
- O método `__repr__` define como o objeto é exibido de forma formal, útil para depuração e desenvolvimento.
- O uso de `!r` em f-strings força a representação formal (`__repr__`), enquanto `!s` força a representação informal (`__str__`).
- Isso permite controlar como os objetos são exibidos em diferentes contextos, tornando o código mais flexível e legível.
"""