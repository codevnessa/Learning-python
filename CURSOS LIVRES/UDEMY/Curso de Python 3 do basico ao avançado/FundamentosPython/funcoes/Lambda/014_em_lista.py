# Funções lambda em listas.

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando uma função lambda para dobrar os números
dobrados = list(map(lambda x: x * 2, numeros))

print(dobrados)  # Resultado: [2, 4, 6, 8, 10]

# 1. `map(lambda x: x * 2, numeros)` aplica a função lambda a cada item da lista.
# 2. A função lambda `lambda x: x * 2` dobra cada número.
# 3. `list(map(...))` converte o resultado de volta para uma lista.
# 4. O resultado ([2, 4, 6, 8, 10]) é exibido.