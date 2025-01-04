# Explicação do conteúdo: Podemos ter tuplas dentro de listas. Isso é útil quando queremos armazenar dados imutáveis (tuplas) dentro de uma estrutura mutável (lista).
# Acessamos os elementos da tupla dentro da lista usando índices duplos: o primeiro para a lista e o segundo para a tupla.

# Exemplo de lista com tuplas:
salas = [
    ("Maria", "Helena"),  # Tupla na posição 0 da lista
    ("Elaine",),          # Tupla na posição 1 da lista
    ("Luís", "João", "Eduarda")  # Tupla na posição 2 da lista
]

# Acessando elementos:
print("Primeira sala:", salas[0])  # Acessa a primeira tupla
print("Primeiro aluno da primeira sala:", salas[0][0])  # Acessa "Maria"
print("Segundo aluno da terceira sala:", salas[2][1])  # Acessa "João"

# Explicação do código:
# 1. A lista `salas` contém tuplas, onde cada tupla representa uma sala com alunos.
# 2. Para acessar um aluno específico, usamos dois índices: o primeiro para a tupla na lista e o segundo para o elemento na tupla.
# OBS: Tuplas são imutáveis, mas a lista que as contém pode ser modificada.