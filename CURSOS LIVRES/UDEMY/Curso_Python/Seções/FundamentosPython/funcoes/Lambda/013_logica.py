# Função lambda para fazer uma verificação lógica.

# Função lambda que verifica se um número é positivo
eh_positivo = lambda x: x > 0

# Usando a função lambda
resultado = eh_positivo(-5)
print(resultado)  # Resultado: False

# 1. `lambda x:` cria uma função lambda que recebe um valor (x).
# 2. `x > 0` é uma expressão lógica que verifica se x é maior que 0.
# 3. `eh_positivo(-5)` chama a função lambda, passando -5 como x.
# 4. O resultado (False) é exibido.