# A função `executa` recebe uma função (`funcao`) e argumentos variáveis (`*args`).
# Ela executa a função passada com os argumentos fornecidos e retorna o resultado.
def executa(funcao, *args):
    return funcao(*args)


# Exemplo 1: Criando uma função `duplica` usando `executa` e lambda.
# A função lambda `lambda m: lambda n: n * m` recebe `m` e retorna uma função que multiplica `n` por `m`.
# Passando `m = 2`, criamos uma função que duplica um número.
m = 2
duplica = executa(lambda m: lambda n: n * m, m)
n = 2
print(f"{m} x {n} = {duplica(n)}")  # Saída: 2 x 2 = 4


# Exemplo 2: Somando dois números com `executa` e lambda.
# A função lambda `lambda x, y: x + y` soma dois números.
# Passando `x = 2` e `y = 3`, o resultado é 5.
x, y = 2, 3
print(f"{x} + {y} =", executa(lambda x, y: x + y, x, y))  # Saída: 5


# Exemplo 3: Somando múltiplos números com `executa` e lambda.
# A função lambda `lambda *args: sum(args)` soma todos os argumentos passados.
# Passando `args = (1, 2, 3, 4, 5, 6, 7)`, o resultado é 28.
args = (1, 2, 3, 4, 5, 6, 7)
print(f"Soma dos números: \n {args} =", executa(lambda *args: sum(args), *args))  # Saída: 28