# __lt__(self,other) - self < other - menor que
# __le__(self,other) - self <= other - menor ou igual
# __gt__(self,other) - self > other - maior que
# __ge__(self,other) - self >= other - maior ou igual
# __eq__(self,other) - self == other - igual
# __ne__(self,other) - self != other - diferente
# __add__(self,other) - self + other - concatenar /  adicionar
# __sub__(self,other) - self - other - subtrair
# __mul__(self,other) - self * other -  multiplicar
# __truediv__(self,other) - self / other - boleano
# __neg__(self) - -self - retorna o oposto lógico
# __str__(self) - str - string - legibilidade
# __repr__(self) - str - string - precisao

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)