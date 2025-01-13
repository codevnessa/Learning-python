"""
Extensão de métodos é uma técnica onde uma classe filha usa o método da classe pai (via `super()`) e adiciona funcionalidades específicas a ele. Isso permite reutilizar o código da classe pai enquanto personaliza o comportamento na classe filha.
"""

# Exemplo de extensão de métodos usando super()

# Classe base (pai)
class Forma:
    def desenhar(self):
        return "Desenhando uma forma genérica"
        # Método que descreve o desenho de uma forma genérica

# Classe derivada (filha)
class Circulo(Forma):
    def desenhar(self):
        return super().desenhar() + " - Especificamente, um círculo"
        # Estende o método da classe pai, adicionando informações específicas sobre o círculo

# Uso
forma = Forma()  # Cria uma instância da classe Forma
circulo = Circulo()  # Cria uma instância da classe Circulo

print(forma.desenhar())  # Saída: Desenhando uma forma genérica
                         # Chama o método da classe Forma

print(circulo.desenhar())  # Saída: Desenhando uma forma genérica - Especificamente, um círculo
                           # Chama o método da classe Circulo, que estende o método da classe Forma

"""
- A classe `Forma` tem um método `desenhar` que descreve o desenho de uma forma genérica.
- A classe `Circulo` herda de `Forma` e usa o método `desenhar` da classe pai, mas adiciona mais informações específicas sobre o círculo.
- Quando você chama `desenhar` em uma instância de `Forma`, ele retorna a mensagem genérica.
- Quando você chama `desenhar` em uma instância de `Circulo`, ele retorna a mensagem genérica mais a parte específica do círculo.
- Isso mostra como você pode reutilizar código da classe pai e adicionar funcionalidades específicas na classe filha.
"""