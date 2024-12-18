from datetime import date
nas = int(input("Ano de nascimento: "))

anoatual = date.today().year
idade = anoatual - nas
genero = int(input("Selecione o seu sexo: "))

gen = {
	1: ("FEMININO"),
	2: ("MASCULINO")
}

while genero == 1:
	print("De acordo com a legislação brasileira, as mulheres nao sao obrigadas a cumprir o alistamento!")
	break
else:
	print("De acordo com a legislação brasileira, os homens devem cumprir o alistamento!")

	if idade < 18:
		print(f"Quem nasceu em {nas} tem {idade} em {anoatual}.")
		print(f"Ainda faltam cerca de {18 - idade} anos para o alistamento.")
		print(f"Seu alistamento será em {nas + 18}!")
	elif idade > 18:
		print(f"Quem nasceu em {nas} tem {idade} em {anoatual}.")
		print(f"Já deveria ter se alistado a {idade - 18} anos atrás.")
		print(f"Seu ano de alistamento foi {anoatual - (idade - 18)}!")
	elif idade == 18:
		print(f"Quem nasceu em {nas} tem {idade} em {anoatual}")
		print(f"Você precisa se alistar IMEDIATAMENTE!")