# Bibliotecas os e json
import os
import json

# Listas para armazenar tarefas e tarefas desfeitas
tarefas = []
tarefas_refazer = []

# Função para salvar tarefas em um arquivo JSON
def salvarTarefa():
    try:
        caminho = os.path.abspath('Curso_Python\\exercicios\\Outros\\tarefas.json')
        print(f'Salvando tarefas em: {caminho}')
        with open(caminho, 'w') as arquivo:
            json.dump(tarefas, arquivo, indent=2)
        print('Tarefas salvas com sucesso!')
    except Exception as e:
        print(f'Erro ao salvar tarefas: {e}')

# Função para carregar tarefas de um arquivo JSON
def carregarTarefas():
    try:
        caminho = os.path.abspath('Curso_Python\\exercicios\\Outros\\tarefas.json')
        if os.path.exists(caminho):
            with open(caminho, 'r') as arquivo:
                return json.load(arquivo)
    except Exception as e:
        print(f'Erro ao carregar tarefas: {e}')
    return []

# Carregar tarefas ao iniciar o programa
tarefas = carregarTarefas()

# Entrada de comandos via terminal
while True:
    print('\nComandos:')
    print('[1] Cadastrar outra tarefa')
    print('[2] Listar Tarefas')
    print('[3] Desfazer tarefa')
    print('[4] Refazer tarefa')
    print('[5] Salvar e Sair')

    try:
        opcao = int(input('Escolha uma opção (1/2/3/4/5): '))
    except ValueError:
        print('Opção inválida! Tente novamente.')
        continue

    # Dicionário de opções com lambdas
    opcoes = {
        1: lambda: tarefas.append(input('Digite a nova tarefa: ').strip()) or print('Tarefa adicionada!'),
        2: lambda: print('Tarefas:\n' + '\n'.join(tarefas) if tarefas else 'Nenhuma tarefa para listar.'),
        3: lambda: (tarefas_refazer.append(tarefas.pop()) if tarefas else print('Nenhuma tarefa para desfazer.')) and print('Última tarefa desfeita!'),
        4: lambda: (tarefas.append(tarefas_refazer.pop()) if tarefas_refazer else print('Nenhuma tarefa para refazer.')) and print('Última tarefa refeita!'),
        5: lambda: salvarTarefa() or print('Saindo...')
    }

    if opcao in opcoes:
        opcoes[opcao]()
        if opcao == 5:
            break
    else:
        print('Opção inválida! Tente novamente.')