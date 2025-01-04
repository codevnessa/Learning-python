# Explicação do conteúdo: Podemos iterar sobre uma lista que contém tuplas, acessando cada elemento das tuplas.
# Isso é útil para processar dados estruturados, como salas com alunos.

# Exemplo de iteração sobre lista com tuplas:
salas = [
    ("Maria", "Helena"),  # Tupla na posição 0 da lista
    ("Elaine",),          # Tupla na posição 1 da lista
    ("Luís", "João", "Eduarda")  # Tupla na posição 2 da lista
]

# Iterando sobre a lista e suas tuplas:
for indice, sala in enumerate(salas):  # Percorre cada tupla na lista
    print(f"Sala {indice}:")
    for aluno in sala:  # Percorre cada aluno na tupla
        print(f"  - {aluno}")

# Explicação do código:
# 1. O loop externo percorre cada tupla na lista, usando `enumerate` para obter o índice da sala.
# 2. O loop interno percorre cada aluno dentro da tupla.
# OBS: Esse padrão é comum para processar dados aninhados.