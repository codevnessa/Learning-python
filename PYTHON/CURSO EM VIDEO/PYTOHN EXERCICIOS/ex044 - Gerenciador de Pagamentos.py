preco = float(input("Preço das compras: R$"))
desc1 = 10
desc2 = 5
juros = 20

def calcular_valores(preco, opcao):
    if opcao == 1:
        avista = preco - (preco * desc1 / 100)
        return avista
    elif opcao == 2:
        cartao = preco - (preco * desc2 / 100)
        return cartao
    elif opcao == 3:
        duasvezes = preco / 2
        return preco, duasvezes
    elif opcao == 4:
        parcela = int(input("Em quantas vezes? "))
        valorjuros = preco + (preco * juros / 100)
        maisdeduas = valorjuros / parcela
        return valorjuros, maisdeduas, parcela
    else:
        return None

def menu():
	while True:
		print("=" * 25)
		print("Loja Apolo")
		print("=" * 25)
		print("[ 1 ] Á vista no dinheiro (10% de desconto)")
		print("[ 2 ] Á vista no cartão (5% de desconto")
		print("[ 3 ] Em 2x no cartão (sem desconto)")
		print("[ 4 ] Em 3x ou mais no cartão (acrescimo de 20%)")

		try:
			opcao = int(input("Escolha uma opção (1/2/3/4): "))
		except ValueError:
			print("Opção invalida! Digite um número valido.")
			continue

		resultado = calcular_valores(preco, opcao)
		if opcao == 1:
			avista = resultado
			print(f"O valor da sua compra de R${preco:.2f}, com pagamento à vista no dinheiro, com desconto de 10%, fica em R${avista:.2f}.")
		elif opcao == 2:
			cartao = resultado
			print(f"O valor da sua compra de {preco}, com pagamento á vista no cartão, com desconto de 5%, fica em R${cartao:.2f}.")
		elif opcao == 3:
			valor_total, duasvezes = resultado
			print(f"O valor da sua compra de R${preco:.2f}, dividido em 2x no cartão, fica em 2 parcelas fixas de R${duasvezes:.2f} cada.")
		elif opcao == 4:
			valor_total, parcela, maisdeduas = resultado
			print(f"O valor da sua compra de R${preco:.2f}, com acréscimo de 20%, fica em R${valor_total:.2f}, em {maisdeduas} parcelas de R${parcela:.2f} cada.")
		return
menu()