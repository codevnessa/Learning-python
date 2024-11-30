# Impressão do nome completo e menu
print('-' * 16 + '   DELIVERY DE COMIDA JAPONESA  ' + '-' * 16)
print('-' * 65)
print('-' * 27 + ' CARDÁPIO ' + '-' * 28)
print('-' * 65)
print('| {:<5} | {:<10} | {:<18} | {:<18} |'.format('V', 'Tamanho', 'Sushi(S)', 'Sashimi(SH)'))
print('| {:<5} | {:<10} | {:<18} | {:<18} |'.format('R', '  P    ', '   R$ 25.00      ', '   R$ 30.00   '))
print('| {:<5} | {:<10} | {:<18} | {:<18} |'.format('F', '  M    ', '   R$ 40.00      ', '   R$ 45.00   '))
print('| {:<5} | {:<10} | {:<18} | {:<18} |'.format('C', '  G    ', '   R$ 55.00      ', '   R$ 60.00   '))
print('-' * 65)

# Inicialização do total do pedido
totalPedido = 0.0

# Dicionário de preços
precos = {
    'S': {'P': 25.0, 'M': 40.0, 'G': 55.0},
    'SH': {'P': 30.0, 'M': 45.0, 'G': 60.0}
}

# Loop principal para pedidos
while True:
    # Menu de opções para sabor
    print("\nEscolha o tipo de comida japonesa:")
    print("[ 1 ] Sushi - S")
    print("[ 2 ] Sashimi - SH")
    sabor_opcao = input("Digite o número da opção desejada: ")

    # Mapeamento das opções para sabores
    if sabor_opcao == '1':
        sabor = 'S'
    elif sabor_opcao == '2':
        sabor = 'SH'
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # Menu de opções para tamanho
    print("\nEscolha o tamanho da porção:")
    print("[ 1 ] Pequena - P")
    print("[ 2 ] Média - M")
    print("[ 3 ] Grande - G")
    tamanho_opcao = input("Digite o número da opção desejada: ")

    # Mapeamento das opções para tamanhos
    if tamanho_opcao == '1':
        tamanho = 'P'
    elif tamanho_opcao == '2':
        tamanho = 'M'
    elif tamanho_opcao == '3':
        tamanho = 'G'
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # Cálculo do valor da comida japonesa
    valorComida = precos[sabor][tamanho]

    # Acumulação do valor total do pedido
    totalPedido += valorComida

    # Impressão do pedido atual
    print(f'Você pediu uma porção de {sabor} no tamanho {tamanho}: R${valorComida}')

    # Pergunta se o cliente deseja pedir mais alguma coisa
    maisPedido = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if maisPedido != 'S':
        break

# Impressão do total do pedido
print(f"Total do pedido: R${totalPedido:.2f}")