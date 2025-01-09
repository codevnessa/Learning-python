import json
from datetime import datetime
import os

# Variáveis globais
id = 10001
lista_tarefas = []

# Função para validar datas
def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Função para carregar tarefas do arquivo JSON
def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar tarefas no arquivo JSON
def salvar_tarefas():
    try:
        caminho_arquivo = os.path.abspath('tarefas.json')
        print(f'Salvando tarefas em: {caminho_arquivo}')
        with open('tarefas.json', 'w') as arquivo:
            json.dump(lista_tarefas, arquivo, indent=4)  # indent=4 para melhorar a legibilidade
        print('Tarefas salvas com sucesso!')
    except Exception as e:
        print(f'Erro ao salvar tarefas: {e}')

def formatar_data(data):
    if len(data) == 8 and data.isdigit():
        data = f"{data[:2]}/{data[2:4]}/{data[4:]}"
    return data

def validar_data(data):
    data = formatar_data(data)
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True, data
    except ValueError:
        return False, None

def cadastrarTarefas():
    global id
    print('\n' + '-' * 20, 'CADASTRO DE TAREFAS', '-' * 20)

    titulo = input('Título da tarefa: ')
    descricao = input('Descrição da tarefa: ')

    datainicio = input('Data de Início (ddmmaaaa ou dd/mm/aaaa): ')
    valido, datainicio_formatada = validar_data(datainicio)
    while not valido:
        print('Formato de data inválido! Use o formato ddmmaaaa ou dd/mm/aaaa.')
        datainicio = input('Data de Início (ddmmaaaa ou dd/mm/aaaa): ')
        valido, datainicio_formatada = validar_data(datainicio)

    dataprevista = input('Data prevista de término (ddmmaaaa ou dd/mm/aaaa): ')
    valido, dataprevista_formatada = validar_data(dataprevista)
    while not valido:
        print('Formato de data inválido! Use o formato ddmmaaaa ou dd/mm/aaaa.')
        dataprevista = input('Data prevista de término (ddmmaaaa ou dd/mm/aaaa): ')
        valido, dataprevista_formatada = validar_data(dataprevista)

    classificacao = input('Classificação:\n[1] Alta prioridade\n[2] Média prioridade\n[3] Baixa prioridade\nEscolha uma opção (1/2/3): ')
    while classificacao not in ['1', '2', '3']:
        print('Opção inválida! Tente novamente.')
        classificacao = input('Escolha uma opção (1/2/3): ')

    tarefa = {
        'id': id,
        'titulo': titulo,
        'descricao': descricao,
        'datainicio': datainicio_formatada,
        'dataprevista': dataprevista_formatada,
        'classificacao': classificacao
    }

    lista_tarefas.append(tarefa)
    id += 1
    salvar_tarefas()
    print('TAREFA CADASTRADA COM SUCESSO!')
    
# Função para consultar tarefas
def consultarTarefas():
    while True:
        print('\n' + '-' * 20, 'CONSULTA DE TAREFAS', '-' * 20)
        print('[1] Consultar todas as tarefas')
        print('[2] Consultar por prioridade')
        print('[3] Consultar ordenadas por data de início')
        print('[4] Consultar ordenadas por data prevista')
        print('[5] Consultar ordenadas por prioridade')
        print('[6] Retornar')

        try:
            opcao = int(input('Escolha uma opção (1/2/3/4/5/6): '))
        except ValueError:
            print('Opção inválida! Tente novamente.')
            continue

        if opcao == 1:
            if not lista_tarefas:
                print('Nenhuma tarefa cadastrada!')
            else:
                print('\n' + '-' * 20, 'TODAS AS TAREFAS', '-' * 20)
                for tarefa in lista_tarefas:
                    exibir_tarefa(tarefa)
        elif opcao == 2:
            consulta_class = input('[1] Alta prioridade\n[2] Média prioridade\n[3] Baixa prioridade\nEscolha uma opção (1/2/3): ')
            while consulta_class not in ['1', '2', '3']:
                print('Opção inválida! Tente novamente.')
                consulta_class = input('Escolha uma opção (1/2/3): ')

            print('\n' + '-' * 20, f'TAREFAS COM PRIORIDADE {consulta_class}', '-' * 20)
            encontrou_tarefa = False
            for tarefa in lista_tarefas:
                if tarefa['classificacao'] == consulta_class:
                    exibir_tarefa(tarefa)
                    encontrou_tarefa = True

            if not encontrou_tarefa:
                print('Nenhuma tarefa encontrada com essa prioridade.')
        elif opcao == 3:
            print('\n' + '-' * 20, 'TAREFAS ORDENADAS POR DATA DE INÍCIO', '-' * 20)
            tarefas_ordenadas = ordenar_tarefas(lista_tarefas, 'datainicio')
            for tarefa in tarefas_ordenadas:
                exibir_tarefa(tarefa)
        elif opcao == 4:
            print('\n' + '-' * 20, 'TAREFAS ORDENADAS POR DATA PREVISTA', '-' * 20)
            tarefas_ordenadas = ordenar_tarefas(lista_tarefas, 'dataprevista')
            for tarefa in tarefas_ordenadas:
                exibir_tarefa(tarefa)
        elif opcao == 5:
            print('\n' + '-' * 20, 'TAREFAS ORDENADAS POR PRIORIDADE', '-' * 20)
            tarefas_ordenadas = ordenar_tarefas(lista_tarefas, 'classificacao')
            for tarefa in tarefas_ordenadas:
                exibir_tarefa(tarefa)
        elif opcao == 6:
            return
        else:
            print('Opção inválida! Tente novamente.')

# Função para exibir uma tarefa
def exibir_tarefa(tarefa):
    classificacao_texto = {
        '1': 'Alta prioridade',
        '2': 'Média prioridade',
        '3': 'Baixa prioridade'
    }
    print(f"ID: {tarefa['id']}")
    print(f"Título: {tarefa['titulo']}")
    print(f"Descrição: {tarefa['descricao']}")
    print(f"Data de início: {tarefa['datainicio']}")
    print(f"Data prevista: {tarefa['dataprevista']}")
    print(f"Classificação: {classificacao_texto[tarefa['classificacao']]}")
    print('-' * 60)

# Função para ordenar tarefas
def ordenar_tarefas(tarefas, criterio):
    if criterio == 'datainicio':
        return sorted(tarefas, key=lambda x: datetime.strptime(x['datainicio'], '%d/%m/%Y'))
    elif criterio == 'dataprevista':
        return sorted(tarefas, key=lambda x: datetime.strptime(x['dataprevista'], '%d/%m/%Y'))
    elif criterio == 'classificacao':
        return sorted(tarefas, key=lambda x: x['classificacao'])
    return tarefas

# Função para editar tarefas
def editarTarefa():
    print('\n' + '-' * 20, 'EDITAR TAREFA', '-' * 20)
    id_tarefa = int(input('Digite o ID da tarefa que deseja editar: '))

    for tarefa in lista_tarefas:
        if tarefa['id'] == id_tarefa:
            print('Deixe em branco para manter o valor atual.')
            titulo = input(f'Título atual: {tarefa["titulo"]}\nNovo título: ') or tarefa['titulo']
            descricao = input(f'Descrição atual: {tarefa["descricao"]}\nNova descrição: ') or tarefa['descricao']
            datainicio = input(f'Data de início atual: {tarefa["datainicio"]}\nNova data de início (dd/mm/aaaa): ') or tarefa['datainicio']
            dataprevista = input(f'Data prevista atual: {tarefa["dataprevista"]}\nNova data prevista (dd/mm/aaaa): ') or tarefa['dataprevista']
            classificacao = input(f'Classificação atual: {tarefa["classificacao"]}\nNova classificação (1/2/3): ') or tarefa['classificacao']

            tarefa['titulo'] = titulo
            tarefa['descricao'] = descricao
            tarefa['datainicio'] = datainicio
            tarefa['dataprevista'] = dataprevista
            tarefa['classificacao'] = classificacao

            salvar_tarefas()  # Salva as alterações no arquivo
            print('TAREFA EDITADA COM SUCESSO!')
            return

    print('Tarefa não encontrada.')

# Função para remover tarefas
def removerTarefa():
    print('\n' + '-' * 20, 'REMOVER TAREFA', '-' * 20)
    id_tarefa = int(input('Digite o ID da tarefa que deseja remover: '))

    for tarefa in lista_tarefas:
        if tarefa['id'] == id_tarefa:
            lista_tarefas.remove(tarefa)
            salvar_tarefas()  # Salva as alterações no arquivo
            print('TAREFA REMOVIDA COM SUCESSO!')
            return

    print('Tarefa não encontrada.')

# Menu principal
def menu_principal():
    global lista_tarefas
    lista_tarefas = carregar_tarefas()  # Carrega as tarefas ao iniciar o programa

    while True:
        print('\n' + '-' * 20, 'MENU PRINCIPAL', '-' * 20)
        print('[1] Cadastrar tarefa')
        print('[2] Consultar tarefas')
        print('[3] Editar tarefa')
        print('[4] Remover tarefa')
        print('[5] Sair')

        try:
            opcao = int(input('Escolha uma opção (1/2/3/4/5): '))
        except ValueError:
            print('Opção inválida! Tente novamente.')
            continue

        if opcao == 1:
            cadastrarTarefas()
        elif opcao == 2:
            consultarTarefas()
        elif opcao == 3:
            editarTarefa()
        elif opcao == 4:
            removerTarefa()
        elif opcao == 5:
            print('Saindo...')
            break
        else:
            print('Opção inválida! Tente novamente.')

# Executa o programa
menu_principal()
salvar_tarefas()