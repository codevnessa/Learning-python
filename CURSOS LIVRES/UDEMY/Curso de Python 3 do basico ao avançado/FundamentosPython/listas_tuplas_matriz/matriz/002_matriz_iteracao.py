# Explicação do conteúdo: Podemos percorrer todos os elementos de uma matriz usando loops aninhados.
# O loop externo itera sobre as linhas, e o loop interno itera sobre os elementos de cada linha.

# Exemplo de iteração sobre uma matriz:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Elementos da matriz:")
for linha in matriz:  # Itera sobre cada linha da matriz
    for elemento in linha:  # Itera sobre cada elemento da linha
        print(elemento, end=" ")  # Imprime o elemento
    print()  # Pula uma linha após cada linha da matriz

# Explicação do código:
# 1. O loop externo percorre cada linha da matriz.
# 2. O loop interno percorre cada elemento da linha atual.
# OBS: A função print(end=" ") evita quebra de linha entre os elementos.