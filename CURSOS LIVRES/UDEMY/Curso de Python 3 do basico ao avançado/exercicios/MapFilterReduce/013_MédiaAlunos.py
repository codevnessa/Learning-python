from functools import reduce

alunos = [
    {'Aluno': 'Lucia', 'Nota': 7.5},
    {'Aluno': 'Maria', 'Nota': 6.9},
    {'Aluno': 'Luiz', 'Nota': 5.3},
    {'Aluno': 'Carol', 'Nota': 7.8},
    {'Aluno': 'Carlos', 'Nota': 5.4},
    {'Aluno': 'Rafael', 'Nota': 9.8},
    {'Aluno': 'Eduardo', 'Nota': 4.9},
    {'Aluno': 'Juliano', 'Nota': 5.7},
    {'Aluno': 'Henrique', 'Nota': 3.4},
    {'Aluno': 'Matheus', 'Nota': 7.3},
    {'Aluno': 'Ricardo', 'Nota': 5.6},
]

sep = '='*20

aprovados = list(filter(lambda n: n['Nota'] >= 7, alunos))
reprovados = list(filter(lambda n: n['Nota'] < 7, alunos))

print('APROVADOS')
for aluno in aprovados:
    print(f"{aluno['Aluno']}: {aluno['Nota']}" )
print(sep)
print(sep)
print('REPROVADOS')
for aluno in reprovados:
    print(f"{aluno['Aluno']}: {aluno['Nota']}" )
print(sep)

quantidade = len(alunos)
soma = reduce(
    lambda acumulador, aluno: acumulador + aluno['Nota'] ,alunos,0
)
resultado = soma / quantidade
print(sep)

print(f'A média dos alunos é: {resultado:.1f}')