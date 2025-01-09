def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def funcaoa(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna

cinco = funcaoa(soma, 5)
dez = funcaoa(multiplica, 10)
print(cinco(10))
print(dez(10))


    