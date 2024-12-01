nome = str(input('Digite seu nome completo: ')).strip().capitalize()
print('Seu nome tem no total {} letras ´A´'.format(nome.count('a')))
print('A letcra ´A´ apareceu pela primeira vez na posição {}.'.format(nome.find('a')+1))
print('A ultima letra a aparece na {} posicao'.format(nome.rfind('a')+1))