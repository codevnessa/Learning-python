def funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Agora voce foi decorada')
        return resultado
    return interna

@funcao
def inverter(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverter('123')

print(invertida)
