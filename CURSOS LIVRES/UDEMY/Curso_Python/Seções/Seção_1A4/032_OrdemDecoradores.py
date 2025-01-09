# Ordem dos decoradores
def parametro(nome):
    def decorador(func):
        print('Decorador:', nome)

        def nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        
        return nova_funcao
    return decorador
@parametro(nome='5')
@parametro(nome='4')
@parametro(nome='3')
@parametro(nome='2')
@parametro(nome='1')
def soma(x, y):
    return x + y
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)


"""

De baixo pra cima

Decorador: 1
Decorador: 2
Decorador: 3
Decorador: 4
Decorador: 5
15 1 2 3 4 5
"""
