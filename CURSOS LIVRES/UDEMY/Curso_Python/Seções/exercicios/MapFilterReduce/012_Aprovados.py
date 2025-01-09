alunos = [
    {'Aluno': 'Lucia', 'Nota': 7.5},
    {'Aluno': 'Maria', 'Nota': 6.9},
    {'Aluno': 'Luiz', 'Nota': 5.3},
    {'Aluno': 'Carol', 'Nota': 9.3}
]

aprovados = list(filter(lambda n: n['Nota'] >= 7, alunos))
reprovados = list(filter(lambda n: n['Nota'] < 7, alunos))

print('APROVADOS')
for aluno in aprovados:
    print(f"{aluno['Aluno']}: {aluno['Nota']}" )

print('REPROVADOS')
for aluno in reprovados:
    print(f"{aluno['Aluno']}: {aluno['Nota']}" )

