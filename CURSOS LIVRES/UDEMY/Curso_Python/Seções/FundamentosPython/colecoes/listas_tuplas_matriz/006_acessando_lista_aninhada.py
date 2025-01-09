# Explicação do conteúdo: Podemos ter listas aninhadas (listas dentro de listas) e acessar seus elementos usando índices múltiplos.
# Isso é útil para estruturas de dados mais complexas.

# Exemplo de lista aninhada:
dados = [
    [1, 2, 3],          # Lista na posição 0 da lista principal
    [4, 5, 6],          # Lista na posição 1 da lista principal
    [7, 8, [9, 10]]     # Lista na posição 2 da lista principal, contendo outra lista
]

# Acessando elementos:
print("Primeira lista:", dados[0])  # Acessa a primeira lista
print("Terceiro elemento da segunda lista:", dados[1][2])  # Acessa 6
print("Segundo elemento da lista aninhada:", dados[2][2][1])  # Acessa 10

# Modificando a lista aninhada:
dados[2][2].append(11)  # Adiciona 11 à lista aninhada
print("Lista aninhada após modificação:", dados[2][2])

# Explicação do código:
# 1. A lista `dados` contém outras listas, incluindo uma lista aninhada na posição 2.
# 2. Para acessar elementos aninhados, usamos múltiplos índices.
# OBS: Listas são mutáveis, então podemos modificar até as listas aninhadas.