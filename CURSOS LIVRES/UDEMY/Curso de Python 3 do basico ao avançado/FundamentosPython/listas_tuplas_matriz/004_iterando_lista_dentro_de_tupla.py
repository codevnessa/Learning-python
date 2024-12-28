# Explicação do conteúdo: Podemos iterar sobre uma tupla que contém listas, acessando cada elemento das listas.
# Isso é útil para processar dados estruturados, como conjuntos de valores.

# Exemplo de iteração sobre tupla com listas:
dados = (
    [10, 20, 30],  # Lista na posição 0 da tupla
    [40, 50, 60],  # Lista na posição 1 da tupla
    [70, 80, 90]   # Lista na posição 2 da tupla
)

# Iterando sobre a tupla e suas listas:
for indice, lista in enumerate(dados):  # Percorre cada lista na tupla
    print(f"Lista {indice}:")
    for valor in lista:  # Percorre cada valor na lista
        print(f"  - {valor}")

# Explicação do código:
# 1. O loop externo percorre cada lista na tupla, usando `enumerate` para obter o índice da lista.
# 2. O loop interno percorre cada valor dentro da lista.
# OBS: Esse padrão é comum para processar dados aninhados.