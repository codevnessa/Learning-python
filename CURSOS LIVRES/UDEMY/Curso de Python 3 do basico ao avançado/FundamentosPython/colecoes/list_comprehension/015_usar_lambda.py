# Criando uma sequência com funções lambda
dobrados = [(lambda x: x * 2)(x) for x in range(5)]

# Exibindo a sequência
print(dobrados)  # Resultado: [0, 2, 4, 6, 8]

# 1. `[(lambda x: x * 2)(x) for x in range(5)]` usa uma função lambda para dobrar os números.
# 2. `lambda x: x * 2` é a função.
# 3. `print(dobrados)` exibe a sequência.