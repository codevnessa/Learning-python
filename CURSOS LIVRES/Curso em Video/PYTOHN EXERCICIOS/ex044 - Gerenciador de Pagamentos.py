# Solicita ao usuário que digite o preço das compras
preco = float(input("Preço das compras: R$"))

# Define os valores dos descontos e juros
desc1 = 10  # Desconto para pagamento à vista no dinheiro
desc2 = 5   # Desconto para pagamento à vista no cartão
juros = 20  # Juros para pagamento em 3x ou mais no cartão

# Define a função calcular_valores que calcula os valores com base na opção escolhida
def calcular_valores(preco, opcao):
    if opcao == 1:
        # Calcula o valor com desconto de 10% para pagamento à vista no dinheiro
        avista = preco - (preco * desc1 / 100)
        return avista
    elif opcao == 2:
        # Calcula o valor com desconto de 5% para pagamento à vista no cartão
        cartao = preco - (preco * desc2 / 100)
        return cartao
    elif opcao == 3:
        # Calcula o valor total e o valor das parcelas para pagamento em 2x no cartão
        duasvezes = preco / 2
        return preco, duasvezes
    elif opcao == 4:
        # Solicita ao usuário o número de parcelas e calcula o valor total com juros e o valor das parcelas
        parcela = int(input("Em quantas vezes? "))
        valorjuros = preco + (preco * juros / 100)
        maisdeduas = valorjuros / parcela
        return valorjuros, maisdeduas, parcela
    else:
        # Retorna None se a opção for inválida
        return None

# Define a função menu que exibe as opções de pagamento e calcula os valores
def menu():
    while True:
        print("=" * 25)
        print("Loja Apolo")
        print("=" * 25)
        print("[ 1 ] Á vista no dinheiro (10% de desconto)")
        print("[ 2 ] Á vista no cartão (5% de desconto)")
        print("[ 3 ] Em 2x no cartão (sem desconto)")
        print("[ 4 ] Em 3x ou mais no cartão (acrescimo de 20%)")

        try:
            # Solicita ao usuário que escolha uma opção de pagamento
            opcao = int(input("Escolha uma opção (1/2/3/4): "))
        except (ValueError, TypeError):
            # Trata o erro se o usuário digitar algo que não seja um número
            print("Opção invalida! Digite um número valido.")
            continue  # Continua o loop para permitir que o usuário tente novamente

        # Calcula os valores com base na opção escolhida
        resultado = calcular_valores(preco, opcao)
        if opcao == 1:
            avista = resultado
            print(f"O valor da sua compra de R${preco:.2f}, com pagamento à vista no dinheiro, com desconto de 10%, fixa em R${avista:.2f}.")
            return
        elif opcao == 2:
            cartao = resultado
            print(f"O valor da sua compra de R${preco:.2f}, com pagamento à vista no cartão, com desconto de 5%, fica em R${cartao:.2f}.")
            return
        elif opcao == 3:
            valor_total, duasvezes = resultado
            print(f"O valor da sua compra de R${preco:.2f}, dividido em 2x no cartão, fica em 2 parcelas fixas de R${duasvezes:.2f} cada.")
            return
        elif opcao == 4:
            valor_total, parcela, maisdeduas = resultado
            print(f"O valor da sua compra de R${preco:.2f}, com acréscimo de 20%, fica em R${valor_total:.2f}, em {maisdeduas} parcelas de R${parcela:.2f} cada.")
            return
        else:
            print("Opção invalida! Escolha uma opção entre 1 e 4.")

# Chama a função menu para iniciar o programa
menu()