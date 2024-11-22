# ESTRUTURA ANINHADA: pois tem formato de ninho estando todos dentro do outro
print('\033[31m-=\033[m'*20)
nome = str(input('\033[1;36mQual o seu nome?\033[m '))
if nome == 'Vanessa':
    print('\033[35mQue nome bonito o seu!\033[m')
elif nome == 'Ana' or nome == 'Pedro' or nome =='Maria':
    print('\033[97mSeu nome é populador no Brasil!!\033[m')
elif nome == '' or nome ==' ':
    print('EI VOCE NAO ESCREVEU SEU NOME, SEU IMBECIL!!!!!!!!!!!!')
elif nome in 'Clara Roberta Juliana Silvana':
    print('Que belo nome!')
#else:
    print('Seu nome é normal, que chato!')
print('\033[36mTenha um bom dia, {}!\033[m'.format(nome))
print('\033[91m-=\033[m'*20)
