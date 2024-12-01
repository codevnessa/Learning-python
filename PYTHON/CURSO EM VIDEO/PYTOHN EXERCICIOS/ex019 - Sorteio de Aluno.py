from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
a5 = input('Quinto aluno: ')
lista = [a1,a2,a3,a4,a5]
es = choice(lista)
print('O aluno escolhido foi {}'.format(es))