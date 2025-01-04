# Como empacotar e desempacotar dicionários em Python, e de usar **kwargs para lidar com argumentos nomeados.

# Código funcional:

# 1. Trocando valores entre variáveis
a, b = 1, 2  # a recebe 1, b recebe 2
a, b = b, a  # Agora, a recebe o valor de b (2) e b recebe o valor de a (1)
# print(a, b)  # Resultado: 2 1

# 2. Desempacotando itens de um dicionário
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

(a1, a2), (b1, b2) = pessoa.items() 

# Desempacota os itens do dicionário
print(a1, a2)  # Resultado: nome Aline
print(b1, b2)  # Resultado: sobrenome Souza
print('-'*10)

# 3. Iterando sobre os itens de um dicionário
for chave, valor in pessoa.items():
     print(chave, valor)  # Exibe cada chave e valor do dicionário
print('-'*10)

# 4. Juntando dois dicionários em um só
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}  # Une os dois dicionários
print(pessoas_completa)  # Resultado: {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}
print('-'*10)

# 5. Função que mostra argumentos nomeados e não nomeados
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)  # Exibe os argumentos não nomeados (args)

    # Exibe os argumentos nomeados (kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)
print('-'*10)

# 6. Usando a função com argumentos nomeados
mostro_argumentos_nomeados(nome='Joana', qlq=123)
# Resultado:
# NÃO NOMEADOS: ()
# nome Joana
# qlq 123
print('-'*10)

# 7. Usando a função com um dicionário desempacotado
mostro_argumentos_nomeados(**pessoas_completa)
# Resultado:
# NÃO NOMEADOS: ()
# nome Aline
# sobrenome Souza
# idade 16
# altura 1.6
print('-'*10)

# 8. Exemplo com mais argumentos nomeados
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}


mostro_argumentos_nomeados(**configuracoes)
# Resultado:
# NÃO NOMEADOS: ()
# arg1 1
# arg2 2
# arg3 3
# arg4 4