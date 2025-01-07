from itertools import groupby

# Lista de alunos com seus nomes e notas
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Função para exibir a lista de alunos
def exibir(alunos):
    for item in alunos:
        print(item)
    print()

# Ordena a lista de alunos pela nota (usando uma função lambda para acessar a chave 'nota')
ordena = sorted(alunos, key=lambda item: item['nota'])

# Exibe a lista ordenada
print("Lista de alunos ordenada por nota:")
exibir(ordena)

# Agrupa os alunos por nota usando a função groupby
# OBS: O groupby só funciona corretamente se os dados estiverem ordenados pela mesma chave usada no agrupamento
grupos = groupby(ordena, key=lambda item: item['nota'])

# Exibe os grupos de alunos por nota
print("Alunos agrupados por nota:")
for chave, grupo in grupos:
    print(f"Nota: {chave}")
    for aluno in grupo:
        print(f"  {aluno['nome']}")
    print()