from perguntas import perguntas;
acertos = 0  # Variável para contar os acertos

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print('Opções:')
    for i, opcao in enumerate(pergunta['Opcoes']):
        print(f'{i+1}) {opcao}')
    
    resposta_usuario = input('Escolha uma opção: ')
    
    # Verifica se o usuário digitou a resposta diretamente
    if resposta_usuario == pergunta['Resposta']:
        print('Resposta correta!\n')
        acertos += 1

    # Verifica se o usuário escolheu uma opção válida
    elif resposta_usuario in ['1', '2', '3', '4']:

        if pergunta['Opcoes'][int(resposta_usuario) - 1] == pergunta['Resposta']:
            print('Resposta correta!\n')
            acertos += 1
        else:
            print('Resposta incorreta!\n')

    else:
        print('Resposta inválida ou incorreta!\n')

# Exibe o total de acertos no final
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')