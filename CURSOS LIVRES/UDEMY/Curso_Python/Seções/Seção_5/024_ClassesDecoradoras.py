class Multiplicar:
    def __init__(self, func):
        print('init')
        self.func = func
        self._multi = 10
    
    def __call__(self, *args, **kwargs):
        print('call')
        resultado = self.func(*args, **kwargs)
        return resultado * self._multi

@Multiplicar
def soma(x,y):
    return x + y

dois = soma(2,2)
print(dois)