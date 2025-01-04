# Criar uma função lambda com um valor padrão:

# Função lambda com valor padrão
multiplicar = lambda x, y=2: x * y

# Usando a função lambda
resultado1 = multiplicar(3)  # Usa o valor padrão de y (2)
resultado2 = multiplicar(3, 4)  # Passa um valor para y (4)

print(resultado1)  # Resultado: 6
print(resultado2)  # Resultado: 12


# 1. `lambda x, y=2:` cria uma função lambda onde y tem um valor padrão de 2.
# 2. Se você não passar um valor para y, ele usa 2.
# 3. `multiplicar(3)` usa o valor padrão de y (2), então 3 * 2 = 6.
# 4. `multiplicar(3, 4)` passa 4 para y, então 3 * 4 = 12.