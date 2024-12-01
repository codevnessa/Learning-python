nome = str(input('Digite seu nome completo:').capitalize().strip())
tem_a = nome.count('a')
if tem_a >= 0:
    print('Seu nome tem no total {} letras ´A´'.format(tem_a))
else:
    print('Seu nome nao tem letras ´A´')