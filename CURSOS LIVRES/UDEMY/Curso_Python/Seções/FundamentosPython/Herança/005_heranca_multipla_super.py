"""
Herança múltipla ocorre quando uma classe herda de mais de uma classe base. O uso de `super()` em herança múltipla segue a ordem definida pelo MRO (Method Resolution Order), garantindo que os métodos das classes base sejam chamados na ordem correta.
"""

# Classe base A
class A:
    def __init__(self):
        print("Inicializando A")
        self.a = "A"
        
# Classe B herda de A
class B(A):
    def __init__(self):
        print("Inicializando B")
        super().__init__()  (C)
        self.b = "B"

# Classe C herda de A
class C(A):
    def __init__(self):
        print("Inicializando C")
        super().__init__()  (A)
        self.c = "C"
      

# Classe D herda de B e C (herança múltipla)
class D(B, C):
    def __init__(self):
        print("Inicializando D")
        super().__init__()  (B)
        self.d = "D"
       

# Uso
d = D()  
print(d.a)   
print(d.b)  
print(d.c)  
print(d.d)  
            # Todos os atributos são acessíveis porque as classes base foram inicializadas corretamente

print(D.mro()) 

"""
- A classe D herda de B e C, que por sua vez herdam de A.
- Quando você cria uma instância de D, o `super()` garante que os métodos `__init__` das classes B, C e A sejam chamados na ordem correta (definida pelo MRO).
- O MRO de D é D -> B -> C -> A, então o `super()` em D chama B, o `super()` em B chama C, e o `super()` em C chama A.
- Isso garante que todos os atributos (a, b, c, d) sejam inicializados corretamente.
- O método `mro()` mostra a ordem em que as classes são processadas, o que ajuda a entender como o Python resolve heranças múltiplas.
"""