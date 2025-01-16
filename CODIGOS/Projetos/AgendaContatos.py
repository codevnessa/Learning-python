id_global = 90001
lista_contatos = []

def cadastrar_contato(id):
    """FUNÇÃO PARA CADASTRAR UM NOVO CONTATO."""
    print('\n' + '-' * 20, 'CADASTRO DE CONTATO', '-' * 20)
    print(f'ID DO CONTATO: {id}')

    # SOLICITA AO USUÁRIO QUE INFORME O NOME, EMAIL E TELEFONE
    nome = input('DIGITE O NOME: ')
    email = input('DIGITE O EMAIL: ')
    telefone = input('DIGITE O TELEFONE: ')

    # CRIA UM DICIONÁRIO PARA O CONTATO
    contato = {'id': id, 'nome': nome, 'email': email, 'telefone': telefone}

    # ADICIONA O CONTATO À LISTA
    lista_contatos.append(contato)
    print('CONTATO CADASTRADO COM SUCESSO!\n')


def consultar_contatos():
    """FUNÇÃO PARA CONSULTAR CONTATOS."""
    while True:
        print('\n' + '-' * 20, 'CONSULTAR CONTATO', '-' * 20)
        print('1 - CONSULTAR TODOS')
        print('2 - CONSULTAR POR ID')
        print('3 - CONSULTAR POR NOME')
        print('4 - RETORNAR AO MENU')

        # SOLICITA AO USUÁRIO QUE ESCOLHA UMA OPÇÃO
        try:
            opcao = int(input('ESCOLHA UMA OPÇÃO (1/2/3/4): '))
        except ValueError:
            print('OPÇÃO INVÁLIDA. POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\n')
            continue

        if opcao == 1:
            # CONSULTA TODOS OS CONTATOS
            print('\n' + '-' * 20, 'TODOS OS CONTATOS', '-' * 20)
            for contato in lista_contatos:
                print(f'ID: {contato["id"]}')
                print(f'NOME: {contato["nome"]}')
                print(f'EMAIL: {contato["email"]}')
                print(f'TELEFONE: {contato["telefone"]}')
                print('-' * 60)

        elif opcao == 2:
            # CONSULTA POR ID
            try:
                id_consulta = int(input('DIGITE O ID DO CONTATO: '))
            except ValueError:
                print('ID INVÁLIDO. POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\n')
                continue
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print('\n' + '-' * 20, 'CONTATO ENCONTRADO', '-' * 20)
                    print(f'ID: {contato["id"]}')
                    print(f'NOME: {contato["nome"]}')
                    print(f'EMAIL: {contato["email"]}')
                    print(f'TELEFONE: {contato["telefone"]}')
                    print('-' * 60)
                    break
            else:
                print('CONTATO NÃO ENCONTRADO.\n')

        elif opcao == 3:
            # CONSULTA POR NOME
            nome_consulta = input('DIGITE O NOME: ')
            print('\n' + '-' * 20, 'CONTATOS ENCONTRADOS', '-' * 20)
            for contato in lista_contatos:
                if contato['nome'].lower() == nome_consulta.lower():
                    print(f'ID: {contato["id"]}')
                    print(f'NOME: {contato["nome"]}')
                    print(f'EMAIL: {contato["email"]}')
                    print(f'TELEFONE: {contato["telefone"]}')
                    print('-' * 60)

        elif opcao == 4:
            # RETORNA AO MENU PRINCIPAL
            return


def remover_contato():
    """FUNÇÃO PARA REMOVER UM CONTATO POR ID."""
    print('\n' + '-' * 20, 'REMOVER CONTATO', '-' * 20)
    try:
        id_remover = int(input('DIGITE O ID DO CONTATO A SER REMOVIDO: '))
    except ValueError:
        print('ID INVÁLIDO. POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\n')
        return

    for contato in lista_contatos:
        if contato['id'] == id_remover:
            lista_contatos.remove(contato)
            print(f'CONTATO COM ID {id_remover} REMOVIDO COM SUCESSO.\n')
            return

    print('CONTATO NÃO ENCONTRADO.\n')


print('-' * 10 + '  SISTEMA DE GERENCIAMENTO DE AGENDA  ' + '-' * 11)
print('-' * 55)
while True:
    print('-' * 19, 'MENU PRINCIPAL', '-' * 20)
    print('1 - CADASTRAR CONTATO')
    print('2 - CONSULTAR CONTATO(S)')
    print('3 - REMOVER CONTATO')
    print('4 - SAIR')

    # SOLICITA AO USUÁRIO QUE ESCOLHA UMA OPÇÃO
    try:
        opcao = int(input('ESCOLHA UMA OPÇÃO (1/2/3/4): '))
    except ValueError:
        print('OPÇÃO INVÁLIDA. POR FAVOR, DIGITE UM NÚMERO VÁLIDO.\n')
        continue

    if opcao == 1:
        # CADASTRA UM NOVO CONTATO
        cadastrar_contato(id_global)
        id_global += 1

    elif opcao == 2:
        # CONSULTA CONTATOS
        consultar_contatos()

    elif opcao == 3:
        # REMOVE UM CONTATO
        remover_contato()

    elif opcao == 4:
        # SAI DO SISTEMA
        print('SAINDO DO SISTEMA...')
        break