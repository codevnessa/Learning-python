# Como criar uma função lambda que aceita vários valores:

# Função lambda que soma todos os números passados
somar_tudo = lambda *args: sum(args)

# Usando a função lambda
resultado = somar_tudo(1, 2, 3, 4)
print(resultado)  # Resultado: 10


# 1. `lambda *args:` cria uma função lambda que aceita vários valores.
# 2. `sum(args)` soma todos os valores passados.
# 3. `somar_tudo(1, 2, 3, 4)` chama a função lambda, passando 4 números.
# 4. O resultado (10) é exibido.