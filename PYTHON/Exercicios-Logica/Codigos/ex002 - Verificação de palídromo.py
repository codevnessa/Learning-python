print("Digite 'sair' a qualquer momento para encerrar o programa.\n")

while True:
	palavra = input("Digite uma palavra: ")

	# Verifica se o usuário quer sair
	if palavra.lower() == 'sair':
		print("\nObrigada por utilizar nosso programa :)")
		print("Esperamos vê-lo novamente em breve!")
		break

	# Verifica se a palavra é um palíndromo
	if palavra == palavra[::-1]:
		print(f"{palavra} é um palíndromo.\n")
	else:
		print(f"{palavra} não é um palíndromo.\n")