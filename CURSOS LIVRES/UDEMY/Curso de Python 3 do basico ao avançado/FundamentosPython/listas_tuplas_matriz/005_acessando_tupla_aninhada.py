# Explicação do conteúdo: Podemos ter tuplas aninhadas (tuplas dentro de tuplas) e acessar seus elementos usando índices múltiplos.
# Isso é útil para estruturas de dados mais complexas.

# Exemplo de tupla aninhada:
dados = (
    (1, 2, 3),          # Tupla na posição 0 da tupla principal
    (4, 5, 6),          # Tupla na posição 1 da tupla principal
    (7, 8, (9, 10))     # Tupla na posição 2 da tupla principal, contendo outra tupla
)

# Acessando elementos:
print("Primeira tupla:", dados[0])  # Acessa a primeira tupla
print("Terceiro elemento da segunda tupla:", dados[1][2])  # Acessa 6
print("Segundo elemento da tupla aninhada:", dados[2][2][1])  # Acessa 10

# Explicação do código:
# 1. A tupla `dados` contém outras tuplas, incluindo uma tupla aninhada na posição 2.
# 2. Para acessar elementos aninhados, usamos múltiplos índices.
# OBS: Tuplas são imutáveis, mas podem conter outras estruturas de dados.