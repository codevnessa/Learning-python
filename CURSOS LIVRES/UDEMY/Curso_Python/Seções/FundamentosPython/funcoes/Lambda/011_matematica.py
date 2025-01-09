# Funções lambda para fazer cálculos matemáticos.

area = lambda largura, altura: largura * altura

# Usando a função lambda
resultado = area(5, 10)
print(resultado)  # Resultado: 50

# 1. `lambda largura, altura:` cria uma função lambda que recebe largura e altura.
# 2. `largura * altura` calcula a área do retângulo.
# 3. `area(5, 10)` chama a função lambda, passando 5 e 10 como valores.
# 4. O resultado (50) é exibido.