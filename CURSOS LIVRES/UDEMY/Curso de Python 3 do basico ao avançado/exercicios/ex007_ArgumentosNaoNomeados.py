def multi(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

resultado = multi(1,6,3,5,9,8,4)
print(resultado)