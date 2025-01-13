def calcular(operador,*args): 
    def duplicar(a): return a * 2
    def triplicar(a): return a  * 3 
    def quadruplicar(a): return a  * 4
    
    operadores ={
        '1' : duplicar,
        '2' : triplicar,
        '3' : quadruplicar,
    }
    resultado = [operadores[operador](numero)for numero in args]
    return resultado
numeros = list(range(81))
resultado = calcular('1', *numeros)
print(resultado)