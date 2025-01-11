"""
MRO (Method Resolution Order) é a ordem em que Python procura métodos em uma hierarquia de classes. Ele define qual método será chamado quando há herança múltipla e métodos com o mesmo nome em classes diferentes. O MRO segue o algoritmo C3, que garante uma ordem consistente e previsível.
"""

# Exemplo básico de MRO (Method Resolution Order)

# Classe base
class A:
    def quem_sou_eu(self):
        return "A"
        # Método da classe base A

# Classe B herda de A
class B(A):
    def quem_sou_eu(self):
        return "B"
        # Método sobrescrito na classe B

# Classe C herda de A
class C(A):
    def quem_sou_eu(self):
        return "C"
        # Método sobrescrito na classe C

# Classe D herda de B e C (herança múltipla)
class D(B, C):
    pass
    # D não sobrescreve o método, então o MRO decide qual método usar

# Uso
d = D()  # Cria uma instância da classe D
print(d.quem_sou_eu())  # Saída: B
                        # O método de B é chamado porque B aparece antes de C no MRO de D

print(D.mro()) 

"""
- Imagine que você tem várias classes: A, B, C e D.
- A classe D herda de B e C, que por sua vez herdam de A.
- Quando você chama um método em D, o Python precisa decidir qual versão do método usar (de B ou C).
- O MRO (Method Resolution Order) é a ordem em que o Python procura o método. Ele segue a ordem D -> B -> C -> A.
- No exemplo, como B aparece antes de C no MRO, o método de B é chamado.
- O método `mro()` mostra essa ordem de busca, que é útil para entender como o Python resolve conflitos em heranças múltiplas.
"""                                                                   