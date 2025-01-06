def gen1():
    print('COMECOU GEN1')  # Início de gen1
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')  # Fim de gen1

def gen3():
    print('COMECOU GEN3')  # Início de gen3
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')  # Fim de gen3

def gen2(gen=None):
    print('COMECOU GEN2')  # Início de gen2
    if gen is not None:
        yield from gen  # Delega para o gerador passado
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')  # Fim de gen2

# Cria geradores combinando gen2 com gen1 e gen3
g1 = gen2(gen1())  # gen2 recebe gen1
g2 = gen2(gen3())  # gen2 recebe gen3
g3 = gen2()        # gen2 sem delegação

# Itera e imprime os valores de g1
for numero in g1:
    print(numero)
print()

# Itera e imprime os valores de g2
for numero in g2:
    print(numero)
print()

# Itera e imprime os valores de g3
for numero in g3:
    print(numero)
print()

"""
yield from gen: Delega a execução para o gerador passado (gen1 ou gen3).

Combinando geradores: gen2 pode encapsular outros geradores ou rodar sozinho.

Saída: Cada bloco de for imprime os valores dos geradores, mostrando a ordem de execução.
"""