# Como criar uma função lambda dentro de outra função:

# Função que retorna uma função lambda
def criar_multiplicador(n):
    return lambda x: x * n

# Criando uma função lambda que multiplica por 3
multiplicar_por_3 = criar_multiplicador(3)

# Usando a função lambda
resultado = multiplicar_por_3(5)
print(resultado)  # Resultado: 15

# 1. `criar_multiplicador(n)` é uma função que retorna uma função lambda.
# 2. A função lambda `lambda x: x * n` multiplica x por n.
# 3. `multiplicar_por_3 = criar_multiplicador(3)` cria uma função lambda que multiplica por 3.
# 4. `multiplicar_por_3(5)` chama a função lambda, passando 5 como x.
# 5. O resultado (15) é exibido.