# Definição da função soma com parâmetros opcionais (x, y, z) e valores padrão None
def soma(x=None, y=None, z=None):
    # Verifica se x ou y são None (ou seja, se não foram fornecidos)
    if x is None or y is None:
        # Se x ou y forem None, imprime uma mensagem de erro e retorna
        print("Pelo menos x e y devem ter valores.")
        return

    # Verifica se z foi fornecido (ou seja, se z não é None)
    if z is not None:
        # Se z foi fornecido, imprime os valores de x, y e z, e a soma dos três
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        # Se z não foi fornecido, imprime os valores de x e y, e a soma dos dois
        print(f'{x=} {y=}', x + y)


# Chamadas da função soma com diferentes argumentos

# 1. x=1, y=2, z=None
soma(1, 2)
# Saída esperada: x=1 y=2 3

# 2. x=3, y=5, z=None
soma(3, 5)
# Saída esperada: x=3 y=5 8

# 3. x=100, y=100, z=100
soma(100, 100, 100)
# Saída esperada: x=100 y=100 z=100 300

# 4. x=100, y='', z=500
soma(100, '', 500)
# Saída esperada: x=100 y= z=500 100500