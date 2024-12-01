nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu primeiro nome é {}.'.format(nome.split()[0]))
print('Seu ultimo nome é {}.'.format(nome.split()[-1]))