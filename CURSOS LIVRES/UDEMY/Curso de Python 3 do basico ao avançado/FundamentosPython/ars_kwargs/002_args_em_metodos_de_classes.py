"""
`*args` também pode ser usado em métodos de classes para aceitar um número variável de argumentos.
Isso é útil quando você quer que um método de uma classe seja flexível em relação ao número de parâmetros que recebe.
"""

class Calculadora:
    def multiplicar(self, *args):
        """
        Este método recebe um número variável de argumentos usando `*args` e retorna o produto deles.
        `*args` é uma tupla que contém todos os argumentos passados para o método.
        """
        resultado = 1
        for numero in args:
            resultado *= numero
        return resultado

calc = Calculadora()
resultado = calc.multiplicar(2, 3, 4)
print(resultado)  # Saída: 24

"""
O método `multiplicar` da classe `Calculadora` usa `*args` para aceitar qualquer número de argumentos e calcular o produto.
Isso mostra como `*args` pode ser aplicado em métodos de classes para aumentar a flexibilidade.
"""