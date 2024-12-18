#FUNÇÃO ESCOLHA DO TIPO DE ROCHA
def escolha_tipo(rochas):
    while True:
        print("Entre com o Tipo de Rocha desejado:")
        for i, (codigo, (nome, preco)) in enumerate(rochas.items(), start=1):
            print(f"[ {i} ]  {codigo}: {nome} - R$ {preco:.2f}/m³")
        try:
            escolha = int(input(">> "))
            if 1 <= escolha <= len(rochas):
                rocha = list(rochas.keys())[escolha - 1]
                nome_rocha, preco_rocha = rochas[rocha]
                print(f"{nome_rocha} selecionada.")
                return rocha, nome_rocha, preco_rocha
            else:
                print("Escolha inválida, entre com o número do modelo novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, entre com um número.")

#FUNÇÃO PARA ESCOLHA DA QUANTIDADE DE BLOCOS
def qtd_blocos():
    while True:
        try:
            quantidade = int(input("\nEntre com a quantidade de blocos (m³): "))
            if 0 < quantidade <= 2000:
                if quantidade < 100:
                    desconto = 0
                elif 100 <= quantidade < 500:
                    desconto = 0.04
                elif 500 <= quantidade < 1000:
                    desconto = 0.09
                elif 1000 <= quantidade <= 2000:
                    desconto = 0.16
                return quantidade, desconto
            else:
                print("Não aceitamos pedidos com essa quantidade de blocos. Por favor, entre com a quantidade novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, entre com um número.")

#FUNÇÃO PARA O TIPO DE TRANSPORTE
def transporte(transportes):
    while True:
        print("Escolha o tipo de Transporte:")
        for i, (nome, preco) in transportes.items():
            print(f"[ {i} ] {nome} - R$ {preco:.2f}")
        try:
            escolha = int(input(">> "))
            if 1 <= escolha <= len(transportes):
                tipo_transporte, preco_transporte = transportes[escolha]
                print(f"{tipo_transporte} selecionado.")
                return preco_transporte
            else:
                print("Escolha inválida, entre com o número do modelo novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, entre com um número.")

#DICIONARIO DA PEDREIRA
def pedreira():
    print('-' * 60)
    print('-' * 21 + '  PEDREIRA LUZIA  ' + '-' * 20)
    print('-' * 60)
    rochas = {
        "MAR": ("Bloco de Mármore", 250.40),
        "GRN": ("Bloco de Granito", 300.20),
        "BAS": ("Bloco de Basalto", 350.90),
        "CAL": ("Bloco de Calcário", 280.10),
        "QUA": ("Bloco de Quartzito", 320.70)
    }

    transportes = {
        1: ("Transporte Rodoviário", 1000.00),
        2: ("Transporte Ferroviário", 2000.00),
        3: ("Transporte Hidroviário", 2500.00)
    }

    rocha, nome_rocha, preco_rocha = escolha_tipo(rochas)
    quantidade, desconto = qtd_blocos()
    preco_transporte = transporte(transportes)

    total_sem_desconto = preco_rocha * quantidade
    total_com_desconto = total_sem_desconto * (1 - desconto)
    total_final = total_com_desconto + preco_transporte

    print(f"\nTotal sem desconto: R$ {total_sem_desconto:.2f}")
    print(f"Desconto: {desconto * 100:.0f}%")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")
    print(f"Custo de transporte: R$ {preco_transporte:.2f}")
    print(f"Total final: R$ {total_final:.2f}")

#EXECUTA O PROGRAMA
pedreira()