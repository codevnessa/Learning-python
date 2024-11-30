ano = int(input("Digite um ano: "))
# Verifica se o ano é divisivel por 4, 100 ou 400 para ser ano b
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
	print(f"{ano} é um ano bissexto")
else:
	print(f"{ano} não é um ano bissexto")